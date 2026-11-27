"""Command-line adapter for application operations."""
import argparse
import getpass
import json
import logging
import os
import sys
import time
import webbrowser
from pathlib import Path
from ..operations import Application


def styled(message, role, stream=None):
    stream = sys.stdout if stream is None else stream
    if not stream.isatty() or 'NO_COLOR' in os.environ or os.environ.get('TERM') == 'dumb':
        return message
    styles = {'heading': '1;36', 'link': '4;36', 'success': '1;32',
              'warning': '1;33', 'error': '1;31', 'muted': '2'}
    return f'\033[{styles[role]}m{message}\033[0m'


def main():
    parser = argparse.ArgumentParser(description='Initialize Data from Oura')
    parser.add_argument('--data-dir', type=Path, default=None, help='Override the configured database directory')
    parser.add_argument('--login', action='store_true', help='Authorize an Oura account after initialization')
    commands = parser.add_subparsers(dest='command')
    sync = commands.add_parser('sync', help='Synchronize Oura data')
    modes = sync.add_subparsers(dest='mode', required=True)
    full = modes.add_parser('full', help='Synchronize all types from a start date')
    full.add_argument('--start', required=True)
    full.add_argument('--end')
    window = modes.add_parser('range', help='Synchronize selected types within a date range')
    window.add_argument('--start', required=True)
    window.add_argument('--end', required=True)
    window.add_argument('--types', nargs='+', required=True)
    incremental = modes.add_parser('incremental', help='Repeat from previous successful windows')
    incremental.add_argument('--end')
    incremental.add_argument('--types', nargs='+')
    incremental.add_argument('--overlap-days', type=int, default=7)
    read = commands.add_parser('read', help='Read local records as JSON')
    read.add_argument('--types', nargs='+')
    read.add_argument('--start')
    read.add_argument('--end')
    read.add_argument('--source-id')
    read.add_argument('--limit', type=int, default=100)
    report = commands.add_parser('report', help='Generate a local report')
    report.add_argument('type', choices=['activity-trend'])
    report.add_argument('--start', required=True)
    report.add_argument('--end', required=True)
    report.add_argument('--force', action='store_true')
    commands.add_parser('profile', help='Show active account')
    args = parser.parse_args()
    if args.login and args.command:
        parser.error('--login cannot be combined with a command')
    try:
        app = Application(args.data_dir)
        logger = logging.getLogger('core')
        if not any(getattr(handler, '_oura_cli', False) for handler in logger.handlers):
            handler = logging.StreamHandler(sys.stderr)
            handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
            handler._oura_cli = True
            logger.addHandler(handler)
        logger.setLevel(app.log_level())
        logger.propagate = False
        if args.command:
            profile = app.current_profile()
            account_id = profile['account_id']
            if args.command == 'profile':
                result = profile
            elif args.command == 'report':
                result = app.report(args.type, args.start, args.end, args.force)
            elif args.command == 'read':
                result = app.read_records(account_id, kinds=args.types, start=args.start,
                                          end=args.end, source_id=args.source_id, limit=args.limit)
            elif args.mode == 'full':
                result = app.sync_full(account_id, args.start, args.end)
            elif args.mode == 'range':
                result = app.sync_range(account_id, args.start, args.end, args.types)
            else:
                result = app.sync_incremental(account_id, args.end, args.types, args.overlap_days)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 1 if args.command == 'sync' and result['status'] != 'succeeded' else 0
        print(styled('Authentication database ready:', 'success'), app.initialize())
        if not args.login:
            print(styled('初始化完成。', 'success') + '连接 Oura 账号请运行：python3 -m core.action --login')
            return 0
        selected, config = app.configuration()
        print(styled('\n[1/3] 准备 Oura 应用凭据', 'heading'))
        print('请登录 ' + styled('https://developer.ouraring.com/applications', 'link') + ' 查看 client ID 和 client secret，或注册新应用。')
        print('Registered redirect URI（已自动配置，无需输入）：' + styled(config['OURA_REDIRECT_URI'], 'link'))
        print(styled('请在 Oura 应用后台登记完全相同的回调地址。', 'warning'))
        prompts = {'OURA_CLIENT_ID': 'Oura client ID: ', 'OURA_CLIENT_SECRET': 'Oura client secret: '}
        if any(not config.get(key) for key in prompts):
            print(styled('请输入缺少的凭据；client secret 输入时不会显示，凭据会保存在本机私有配置中。', 'muted'))
        else:
            print(styled('已找到本机配置的应用凭据，无需重复输入。', 'success'))
        missing = {}
        for key, prompt in prompts.items():
            if not config.get(key):
                value = (getpass.getpass(styled(prompt, 'heading', sys.stderr)) if key == 'OURA_CLIENT_SECRET'
                         else input(styled(prompt, 'heading'))).strip()
                if not value:
                    raise ValueError(f'{key} is required')
                missing[key] = value
        if missing:
            _, config = app.save_configuration(selected, missing)
            print(styled('应用凭据已保存。', 'success'))
        login = app.login(config)
        try:
            with login:
                print(styled('\n[2/3] 在浏览器中授权 Oura 账号', 'heading'), flush=True)
                print('授权 URL：\n' + styled(login.url, 'link'), flush=True)
                print(styled('将在 3 秒后自动打开浏览器。如果 3 秒后没有自动打开，请复制上方 URL 到浏览器完成这一步。', 'warning'), flush=True)
                print(styled('请允许访问个人信息，以便识别账号。浏览器打开后有 60 秒完成授权和账号保存。', 'muted'), flush=True)
                for remaining in range(3, 0, -1):
                    print(styled(f'{remaining} 秒后打开浏览器…', 'muted'), flush=True)
                    time.sleep(1)
                try:
                    opened = webbrowser.open(login.url)
                except (webbrowser.Error, OSError):
                    opened = False
                if not opened:
                    print(styled('未能自动打开浏览器，请手动打开上方授权 URL。', 'warning'), flush=True)
                account = login.complete(timeout=60, report=lambda remaining: print(styled(f'等待授权和账号保存，剩余 {remaining} 秒…', 'muted'), flush=True))
                print(styled('\n[3/3] 账号已保存', 'heading'), flush=True)
                print(styled(f'Account initialized: {account}', 'success'), flush=True)
                print(styled('登录成功。回调页面收到授权后会倒计时 3 秒尝试关闭；回调服务将在 5 秒后自动关闭。', 'success'), flush=True)
                try:
                    for remaining in range(5, 0, -1):
                        print(styled(f'{remaining} 秒后关闭回调服务…', 'muted'), flush=True)
                        time.sleep(1)
                except KeyboardInterrupt:
                    print(styled('\n正在关闭回调服务…', 'muted'), flush=True)
        finally:
            print(styled('回调服务已关闭。', 'success'), flush=True)
        return 0
    except TimeoutError:
        print(styled('登录超过 60 秒，尚未完成。请重新运行 python3 -m core.action --login。', 'error', sys.stderr), file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print(styled('\n已取消登录，可重新运行 python3 -m core.action --login。', 'warning', sys.stderr), file=sys.stderr)
        return 130
    except (ValueError, RuntimeError, OSError, KeyError) as error:
        message = str(error) if isinstance(error, (ValueError, RuntimeError)) else type(error).__name__
        print(styled('Command failed: ' + message, 'error', sys.stderr), file=sys.stderr)
        return 1
