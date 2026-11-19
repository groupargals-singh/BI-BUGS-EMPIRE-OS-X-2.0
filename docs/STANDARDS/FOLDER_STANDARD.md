# Folder Standard

**Status:** Draft standard; verify against the actual repository before restructuring.

Canonical sources: `../MASTER_SPECIFICATION/07_PROJECT_STRUCTURE.md` and `../MASTER_SPECIFICATION/08_FOLDER_ARCHITECTURE.md`.

- Give each directory one clear responsibility and an identifiable owner.
- Keep source, tests, documentation, generated artifacts, runtime data, and secrets separated.
- Avoid ambiguous duplicate folders and undocumented cross-module ownership.
- Document public entry points, dependencies, and expected contents for non-obvious directories.
- Do not move or rename existing files until imports, build scripts, deployments, and references have been checked.