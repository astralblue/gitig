# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`gitig` is a Python CLI tool for composing and synchronizing .gitignore files from GitHub's template collection. It reads existing .gitignore files with specially formatted marker comments and can update/add template sections from github/gitignore repository.

## Commands

### Development Environment
- **Package manager**: `uv` (recommended) or `pip`
- **Install dependencies**: `uv sync` or `pip install -e .[dev]`
- **Run the tool**: `python -m gitig` or `gitig` (when installed)

### Code Quality
- **Format code**: `black .` (configured in pyproject.toml)
- **Sort imports**: `isort .` (configured with black profile)
- **Lint code**: `ruff check .` (configured in dependency-groups.dev)
- **Run all formatters**: `black . && isort .`

### Testing
- **Test framework**: `pytest` (configured in dev dependencies)
- **Run tests**: `pytest` 
- **Run with coverage**: `pytest --cov=gitig`

### Build and Distribution
- **Build backend**: `flit_core` (configured in pyproject.toml)
- **Build package**: `python -m build` or `flit build`
- **Install from source**: `pip install -e .`

## Architecture

### Core Components

#### Main Module (`gitig/__init__.py`)
- **Entry point**: `main()` function handles CLI parsing and orchestration
- **Core logic**: `async_main()` processes .gitignore files with template synchronization
- **Template markers**: Uses regex pattern to identify BEGIN/END sections with format:
  ```
  # --- BEGIN https://raw.githubusercontent.com/github/gitignore/{SHA}/{TEMPLATE}.gitignore ---
  # --- END https://raw.githubusercontent.com/github/gitignore/{SHA}/{TEMPLATE}.gitignore ---
  ```

#### Network Module (`gitig/net.py`)
- **Template fetching**: `get_template()` downloads templates from GitHub raw URLs
- **SHA resolution**: `get_latest_sha()` finds latest commit affecting a template using GitHub API
- **HTTP client**: Uses `httpx` with context variable for async client management
- **GitHub API**: Uses `PyGithub` for repository operations

#### Logging Module (`gitig/_logging.py`)
- **Structured logging**: `StructLogAdapter` provides structured logging with bound context
- **Output formats**: Console (Rich) and JSON logging modes
- **Extra fields**: Custom formatter for additional context fields

#### Constants (`gitig/consts.py`)
- **GitHub repository**: `github/gitignore`
- **Raw URL base**: Template for fetching raw files

#### Utilities (`gitig/utils.py`)
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