"""Encrypt local credentials with a key stored in the system keyring."""


def encryption_key(root, has_credentials=False):
    try:
        import keyring
        from cryptography.fernet import Fernet
    except ImportError as e:
        raise RuntimeError('Login requires dependencies: pip install -r requirements.txt') from e
    service = 'data-from-oura'
    name = str(root.resolve())
    key = keyring.get_password(service, name)
    if not key:
        if has_credentials:
            raise RuntimeError('Encryption key missing from system keyring; restore it before login')
        key = Fernet.generate_key().decode()
        keyring.set_password(service, name, key)
    fernet = Fernet(key.encode())
    return lambda token: fernet.encrypt(token.encode())


