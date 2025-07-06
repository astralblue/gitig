# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`ign` is a Python CLI tool for composing and synchronizing .gitignore files from GitHub's template collection. It reads existing .gitignore files with specially formatted marker comments and can update/add template sections from github/gitignore repository.

**Status**: ✅ **RELEASED v0.1.0** - Published on PyPI at https://pypi.org/project/ign/
**Repository**: https://github.com/astralblue/ign

## Commands

### Development Environment
- **Package manager**: `uv` (recommended) or `pip`
- **Install dependencies**: `uv sync` or `pip install -e .[dev]`
- **Run the tool**: `python -m ign` or `ign` (when installed)

### Code Quality
- **Format and lint code**: `ruff format . && ruff check --fix .` (handles formatting, linting, and import sorting)
- **Run all quality checks**: `ruff format . && ruff check --fix .`
- **Note**: Black has been removed as a dependency; Ruff handles all code quality tasks

### Release Management

**Hybrid Approach**: Manual changelog + Automated versioning

#### Automated Components
- **Version bumping**: `semantic-release` reads commit messages and bumps version automatically
- **GitHub releases**: Created automatically with auto-generated release notes from commits
- **PyPI publishing**: Automatic when version changes
- **Documentation**: `docs/changelog.rst` updated automatically from `CHANGELOG.md`

#### Manual Components  
- **CHANGELOG.md**: Manually maintained using `kacl-cli` for high-quality entries
- **Release notes**: Manual changelog provides detailed, curated release information

#### Versioning Scheme (Pre-1.0)
- `feat!:` or `BREAKING CHANGE:` → Minor bump (0.1.x → 0.2.0) 
- `feat:` → Patch bump (0.1.1 → 0.1.2)
- `fix:`, `perf:`, etc. → Patch bump (0.1.1 → 0.1.2)

#### Manual Changelog Commands
- **Validate**: `kacl-cli verify` (validates Keep a Changelog format)
- **Add entries**: `kacl-cli add [added|changed|fixed|removed] "description"`
- **Create release**: `kacl-cli release X.X.X` (moves Unreleased to versioned section)
- **Update docs**: `python scripts/update-changelog.py` (converts CHANGELOG.md to docs/changelog.rst)

#### Workflow
1. Use `kacl-cli add` to manually curate important changes in CHANGELOG.md
2. Commit with conventional commit messages for automatic versioning
3. Push to main → GitHub Actions automatically releases based on commit messages
4. Manual CHANGELOG.md provides detailed release notes, commit-based changelog provides GitHub release notes

#### Tools
- `python-semantic-release` for automated version management and GitHub releases
- `python-kacl` for manual changelog curation
- `m2r2` for Markdown→reStructuredText conversion
- GitHub Actions for CI/CD automation

### Testing
- **Test framework**: `pytest` (configured in dev dependencies)
- **Run tests**: `pytest` 
- **Run with coverage**: `pytest --cov=ign`

### Build and Distribution
- **Build backend**: `flit_core` (configured in pyproject.toml)
- **Build package**: `flit build`
- **Publish to PyPI**: `flit publish`
- **Install from PyPI**: `pip install ign` or `uv add ign`
- **Install from source**: `pip install -e .`

### Release Management
- **Automated releases**: `python-semantic-release` for version management and GitHub releases
- **Standard workflow**: `uv run semantic-release version` (uses standard tags `v{version}`)
- **Local workflow**: `uv run semantic-release -c pyproject-local.toml version` (uses prefixed tags `astralblue/v{version}`)
- **Manual changelog**: Use `kacl-cli` for Keep a Changelog format maintenance
- **Automatic RST conversion**: `scripts/update-changelog.py` converts CHANGELOG.md to docs/changelog.rst
- **Hybrid approach**: Manual changelog curation + automated versioning and publishing

## Architecture

### Core Components

#### Main Module (`ign/__init__.py`)
- **Entry point**: `main()` function handles CLI parsing and orchestration
- **Core logic**: `async_main()` processes .gitignore files with template synchronization
- **Template markers**: Uses regex pattern to identify BEGIN/END sections with format:
  ```
  # --- BEGIN https://raw.githubusercontent.com/github/gitignore/{SHA}/{TEMPLATE}.gitignore ---
  # --- END https://raw.githubusercontent.com/github/gitignore/{SHA}/{TEMPLATE}.gitignore ---
  ```

#### Network Module (`ign/net.py`)
- **Template fetching**: `get_template()` downloads templates from GitHub raw URLs
- **SHA resolution**: `get_latest_sha()` finds latest commit affecting a template using GitHub API
- **HTTP client**: Uses `httpx` with context variable for async client management
- **GitHub API**: Uses `PyGithub` for repository operations

#### Logging Module (`ign/_logging.py`)
- **Structured logging**: `StructLogAdapter` provides structured logging with bound context
- **Output formats**: Console (Rich) and JSON logging modes
- **Extra fields**: Custom formatter for additional context fields

#### Constants (`ign/consts.py`)
- **GitHub repository**: `github/gitignore`
- **Raw URL base**: Template for fetching raw files

#### Utilities (`ign/utils.py`)
- **Final metaclass**: `FinalMeta` prevents class inheritance

### Key Algorithms

#### Template Synchronization Strategy
1. **Parse existing**: Extract template sections from current .gitignore
2. **Fetch versions**: Get old version (from markers) and new version (latest)
3. **Diff application**: Try two merge strategies:
   - Strategy A: Apply (new - old) diff to local modifications
   - Strategy B: Apply (local - old) diff to new template
4. **Conflict resolution**: Falls back gracefully when patches fail

#### Marker Processing
- Uses state machine to track BEGIN/END marker pairs
- Validates marker consistency (matching template names and SHAs)
- Preserves local modifications between template sections

### Environment Variables
- **GITHUB_API_TOKEN**: Optional GitHub API token for higher rate limits
- **Standard dotenv**: Loads from .env file automatically

### CLI Interface
- **Input/Output**: Supports stdin/stdout with `-` or file paths
- **Dry run**: `--dry-run/-n` for preview mode
- **Diff output**: `--diff/-d` shows unified diff
- **Template specification**: `TEMPLATE[@HASH]` format for specific versions
- **Auto-detection**: Automatically detects existing templates if none specified

### Error Handling
- **Structure errors**: Returns `os.EX_DATAERR` for malformed template markers
- **Network errors**: Graceful handling of GitHub API failures
- **Custom exceptions**: `NoCommitError` for missing template commits

## Release History

### Post-v0.1.4 Improvements (2025-07-06)
- **Release automation perfection**: Configured semantic-release with automatic RST conversion
- **Local workflow support**: Created pyproject-local.toml for prefixed tag workflow compatibility
- **kacl-cli integration**: Resolved format compatibility between semantic-release and Keep a Changelog
- **Hybrid documentation**: Manual CHANGELOG.md curation + automated docs/changelog.rst generation
- **Streamlined CI/CD**: Removed manual conversion steps, semantic-release handles everything

### Post-v0.1.0 Improvements (2025-07-06)
- **Logging enhancements**: Default to INFO level, improved CLI options (`-q`/`--quiet` added)
- **Auto-detection**: JSON logging when stderr is not a TTY
- **Performance**: Added LRU caching for template fetching with `async-lru`
- **Bug fixes**: Fixed double logging when using `-v` and `-d` together
- **Code quality**: Fully migrated to Ruff-only workflow (removed Black dependency)
- **Dependencies**: Moved dev dependencies to PEP 735 dependency groups
- **Documentation**: Updated with new CLI options and recent improvements
- **Release automation**: Added python-kacl for changelog management, m2r2 for Markdown→RST conversion, and python-semantic-release for automated versioning
- **CI/CD**: Added GitHub Actions workflows for automated testing and releases
- **Documentation**: Added Read the Docs integration with automatic builds

### v0.1.0 (2025-07-06)
- **Initial release** published to PyPI
- **Project renamed** from `gitig` to `ign` (gitig was taken on PyPI)
- **Repository moved** to https://github.com/astralblue/ign
- **Code quality** consolidated to Ruff (formatting + linting + import sorting)
- **Full documentation** with Sphinx, comprehensive README.rst
- **Core features**: Template synchronization, dual merge strategies, GitHub API integration