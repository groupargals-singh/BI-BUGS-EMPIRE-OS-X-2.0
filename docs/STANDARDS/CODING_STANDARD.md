# Coding Standard

**Status:** Draft standard; language-specific standards may add detail.

Canonical sources: `../MASTER_SPECIFICATION/06_ENGINEERING_RULES.md` and `../MASTER_SPECIFICATION/18_TESTING.md`.

- Use consistent formatting and descriptive names; keep functions and modules focused.
- Document public contracts, side effects, errors, configuration, and security assumptions.
- Prefer typed/schema-validated interfaces where supported by the chosen language.
- Avoid dead code, hidden global state, duplicated policy logic, and swallowed exceptions.
- Add deterministic tests for normal, boundary, failure, and permission-denied behavior.
- Run project format/lint/test commands and record versions and results.