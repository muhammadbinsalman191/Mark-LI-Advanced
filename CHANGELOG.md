# Changelog

All notable derivative changes to Mark-LI Advanced should be documented here.

This changelog is for changes made in this repository. It does not attempt to reproduce the upstream MARK LI changelog.

## Unreleased

### Added

- Derivative-specific repository documentation and clearer upstream attribution
- Real Core Mode and Command Center screenshots
- Contribution and security guidance
- GitHub Issue templates and project roadmap
- Repeatable startup smoke test in `tests/smoke_startup.py`
- Contributor instructions for running the startup smoke test
- Python 3.12.x target documentation, with Python 3.12.10 recorded as the currently verified environment
- Setup-time Python version validation

### Fixed

- Removed duplicate F11 fullscreen shortcut registration
- Removed duplicate Escape interrupt shortcut registration

### Maintenance

- Made `jarvis-advanced` the default development branch
- Began tracking maintenance work through GitHub Issues
- Adopted focused pull-request workflows for repository changes

### Existing derivative work

- Core / Command Center UI-mode control in the `jarvis-advanced` branch
- Core protocol / prompt refinements
- Runtime-memory protection work
