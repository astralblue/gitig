# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Configured semantic-release to automatically run md-to-rst conversion
- Created pyproject-local.toml for prefixed tag workflow compatibility
- Resolved kacl-cli format compatibility with Keep a Changelog standard

### Changed
- Modified release automation to work with both semantic-release and kacl-cli
- Removed manual conversion steps from GitHub Actions workflow

## [0.1.4] - 2025-07-06

### Fixed
- Improved changelog RST automation for Read the Docs integration
- Updated docs/changelog.rst with latest releases (0.1.2, 0.1.3)
- Fixed GitHub Actions changelog update with better error handling
- Used correct remote name (astralblue) in git push

## [0.1.3] - 2025-07-06

### Fixed
- Added flit to dev dependencies for CI builds
- Retired build dependency group and consolidated all build tools into dev dependencies

## [0.1.2] - 2025-07-06

### Added
- Comprehensive release automation with CI/CD pipeline
- Pre-1.0 semantic versioning scheme configuration
- Hybrid changelog approach combining automation and manual curation

### Fixed
- Disabled build command in semantic-release to avoid container dependency issues
- Used flit build instead of python -m build for better compatibility
- Handled missing tests in CI workflows gracefully
- Formatted scripts/update-changelog.py with ruff

## [0.1.1] - 2025-07-06

### Added
- Template caching for improved performance using async-lru
- Quiet mode (`-q`/`--quiet`) CLI option
- Auto-detection of TTY for logging format (JSON when stderr is not a tty)

### Changed
- Default logging level to INFO to display useful progress messages
- Verbose option (`-v`) now enables DEBUG messages
- Streamlined logging throughout the application

### Fixed
- Double logging issue when using `-v` and `-d` together

## [0.1.0] - 2025-07-05

### Added
- Initial release of ign (renamed from gitig due to PyPI name conflict)
- Core gitignore template synchronization functionality
- Dual merge strategies for conflict resolution
- GitHub API integration for template fetching
- Support for conventional commits and semantic versioning
- Comprehensive documentation with Sphinx
- CLI with support for stdin/stdout, dry-run, and diff modes

### Changed
- Consolidated to Ruff for all code quality tasks (formatting, linting, import sorting)
- Moved from setup.py to pyproject.toml with flit_core build backend
- Used uv for dependency management

[Unreleased]: https://github.com/astralblue/ign/compare/v0.1.4...HEAD
[0.1.4]: https://github.com/astralblue/ign/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/astralblue/ign/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/astralblue/ign/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/astralblue/ign/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/astralblue/ign/releases/tag/v0.1.0
