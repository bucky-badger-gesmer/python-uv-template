# 🐍 Python Project Template with uv & Ruff

Welcome! This is a minimal Python project template to help you write clean, manageable Python code with uv, Ruff, and ty.

---

## 📦 Prerequisites

### Install uv

Installation guide for uv can be found [here](https://docs.astral.sh/uv/getting-started/installation/)

Verify that it has been successfully installed by running:

```
uv
```

### Adding/Removing a package

To add a package, run:

```
uv add <PACKAGE_NAME>
```

To remove a package, run:

```
uv remove <PACKAGE_NAME>
```

### Linting & Formatting with Ruff

To lint files, run:

```
uvx ruff check
```

To format files, run:

```
uvx ruff format
```

### Type checking with ty

To type check files, run:

```
uvx ty check
```

Useful links:

- https://docs.astral.sh/uv/
- https://docs.astral.sh/ruff/
- https://docs.astral.sh/ruff/rules/
- https://docs.astral.sh/ty/
