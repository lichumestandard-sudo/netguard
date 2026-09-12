# Contributing to NetGuard

Thanks for your interest in NetGuard! This started as a Cybersecurity
elective coursework project, but contributions and suggestions are welcome.

## Getting Started

1. Fork the repository
2. Clone your fork and install in editable mode:
```bash
   git clone https://github.com/YOUR_USERNAME/netguard.git
   cd netguard
   pip install -e .[dev]
```
3. Run the test suite to confirm everything passes:
```bash
   pytest -v
```

## Making Changes

- Keep functions small and focused, matching the existing module structure (one feature per file under `netguard/`).
- Add or update tests in `tests/` for any new logic, especially pure functions like parsing or validation.
- Run `pytest` before opening a pull request.
- Follow the existing docstring style (short summary, `Args`/`Returns` where relevant).

## Reporting Issues

If you find a bug or have a feature request, please open an issue describing:
- What you expected to happen
- What actually happened
- Steps to reproduce (OS, Python version, command used)

## Code of Conduct

Be respectful and constructive. This is a learning project, so patience with imperfect code is appreciated.
