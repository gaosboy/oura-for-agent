# Oura Skill packaging plan

Goal: produce a portable, versioned Skill containing only application runtime resources.

1. Maintain a separate packaging manifest and explicit runtime file allowlist; build a Skill directory and ZIP under `build/`, and check versions before replacement.
2. Provide an idempotent setup script that prepares a virtual environment and calls the application CLI to initialize the database. Describe interactive OAuth setup and all exposed CLI operations in the Skill.
3. Test packaging exclusions, version checks, archive structure, and initialization from an extracted artifact with isolated data. Run the full test suite and Skill validator.
