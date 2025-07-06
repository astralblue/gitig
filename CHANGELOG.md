# CHANGELOG


## v0.1.2 (2025-07-06)

### Bug Fixes

* fix: disable build command in semantic-release

- Set build_command to empty string to skip building in semantic-release
- Building will be handled separately in GitHub Actions workflow
- This avoids dependency issues in the semantic-release container ([`977cb6d`](https://github.com/astralblue/ign/commit/977cb6d0350546f5045fdee885a0adf3f19ae077))

* fix: use flit build instead of python -m build

- Replace python -m build with flit build in semantic-release config
- Update GitHub Actions workflow to use flit build
- Remove build dependency as we use flit directly ([`e3137c1`](https://github.com/astralblue/ign/commit/e3137c16cf0edd2bef66c8abc61bd6bb8a453ef3))

* fix: format scripts/update-changelog.py with ruff ([`d39b328`](https://github.com/astralblue/ign/commit/d39b32842b6c2ff546388daddfe9ddc410d40f4b))

* fix: handle missing tests in CI workflows

- Allow pytest to exit gracefully when no tests are found
- This prevents CI failure during development phase
- Add fallback message for empty test suites ([`0433f7b`](https://github.com/astralblue/ign/commit/0433f7b16aeee8fa7f69bf973f11dd87e6765c88))

### Features

* feat: implement hybrid changelog approach

- Configure semantic-release for version bumping only (not changelog)
- Keep manual CHANGELOG.md management with kacl-cli
- Separate PyPI publishing from semantic-release
- Update documentation with hybrid workflow explanation
- Auto-generated release notes from commits, manual changelog for docs

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com> ([`bedea4b`](https://github.com/astralblue/ign/commit/bedea4bd551bbff2d1aa2f17fdc594b01c9c752e))

* feat: configure pre-1.0 semantic versioning scheme

- Set major_on_zero=false and allow_zero_version=true
- Configure breaking changes (feat\!) to bump minor version
- Configure features and fixes to bump patch version
- Update documentation with 0.x versioning scheme

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com> ([`e09631f`](https://github.com/astralblue/ign/commit/e09631f1059eb1e546d3cfcd0e975904ce5f4c07))

* feat: add comprehensive release automation with CI/CD

- Add python-semantic-release for automated version management
- Configure GitHub Actions workflows for testing and releases
- Add Read the Docs configuration for automated documentation
- Update CLAUDE.md with new release management tools
- Enable automatic PyPI publishing and GitHub releases

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com> ([`32ce01b`](https://github.com/astralblue/ign/commit/32ce01b9d7037420e51c4fd5d90a2ec80ef6c2a3))

* feat: add release automation tooling with python-kacl and m2r2

- Add python-kacl for changelog automation and validation
- Add m2r2 for Markdown to reStructuredText conversion
- Create scripts/update-changelog.py for automated docs sync
- Fix CHANGELOG.md format to comply with Keep a Changelog
- Update docs/changelog.rst with current content

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com> ([`d120b5e`](https://github.com/astralblue/ign/commit/d120b5ec5c76205036e88d0c2c50972ef2e1ae26))


## v0.1.1 (2025-07-06)

### Bug Fixes

* fix: double logging when using -v and -d together ([`b0ed563`](https://github.com/astralblue/ign/commit/b0ed56364075cfcd8a3aa8b45b236b55b6689cdb))

### Chores

* chore: update CLAUDE.md with recent improvements

- Document post-v0.1.0 enhancements in release history
- Update CLI logging improvements and new options
- Note removal of Black dependency in favor of Ruff-only workflow
- Document performance improvements with template caching
- Record bug fixes and dependency management changes

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com> ([`bebb5a5`](https://github.com/astralblue/ign/commit/bebb5a595f6dac479a2eee4d881a9552b5f1d2b8))

* chore: remove uv as a runtime dependency ([`90e82d1`](https://github.com/astralblue/ign/commit/90e82d17cdfc405f7a6da5ce6453917bf56000d5))

* chore: simplify by using just Ruff ([`67013b6`](https://github.com/astralblue/ign/commit/67013b6da49919fc8981791ba01b9c9ae0fec9cf))

* chore: move dev dependencies to PEP 735 dependency group

This is in line with what uv uses with the --dev flag. ([`2b60ba1`](https://github.com/astralblue/ign/commit/2b60ba1a8e0189c2dbfd17d6e15358f1c76913fa))

* chore: exclude build output dirs in PyCharm ([`45155b0`](https://github.com/astralblue/ign/commit/45155b06227591645b2eef382fffb05074077700))

### Documentation

* docs: update documentation with recent improvements

- Update CLI option descriptions for new logging behavior
- Document quiet mode and improved verbose/debug options
- Add changelog entries for post-v0.1.0 improvements
- Update development guide to reflect Ruff-only workflow
- Document template caching and performance improvements

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com> ([`4c42c12`](https://github.com/astralblue/ign/commit/4c42c129b9b7158cd07569e47003f94b78fe3ee5))

* docs: add missing punctuation ([`79ad885`](https://github.com/astralblue/ign/commit/79ad885f58937db79884855043a4ded871ed985a))

* docs: don't recommend uv for installation

uv may be great for development but is an overkill for installing CLIs. ([`4161a21`](https://github.com/astralblue/ign/commit/4161a210244fab3033f30baf30041f334b24a266))

* docs: update CLAUDE.md with v0.1.0 release status

- Add release status and PyPI link
- Document publishing workflow
- Add release history section
- Update repository references

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com> ([`f941869`](https://github.com/astralblue/ign/commit/f9418693853522d1dc5321b4a0201c51b97b9efb))

### Features

* feat: use JSON logging if stderr is not a tty ([`0d0220a`](https://github.com/astralblue/ign/commit/0d0220a3cc806dd25a69f657f502ab0150ecf828))

* feat: streamline logging CLI options

- Default to INFO level to display useful progress messages.
- Make -v enable DEBUG messages.
- Add -q/--quiet for the old behavior (WARNING level). ([`acae32a`](https://github.com/astralblue/ign/commit/acae32a31fcd9ce46ba3b1e38e56814ce4154a2f))

* feat: streamline logging

- Log useful progress messages at INFO level.
- Demote verbose log messages to DEBUG level.
- Do log when updating/adding templates. ([`099fff7`](https://github.com/astralblue/ign/commit/099fff717fc23129f54f8a9c58b00d40698e9aa6))

* feat: cache fetched templates ([`89d53bd`](https://github.com/astralblue/ign/commit/89d53bd894d50bb6a367f41ecfc14b75d6cf42d3))

### Unknown

* Release version 0.1.1

- Template caching for improved performance
- Quiet mode and improved logging options
- Auto-detection of TTY for logging format
- Bug fixes for double logging issue
- Simplified to Ruff-only code quality workflow
- Documentation updates

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com> ([`35b972d`](https://github.com/astralblue/ign/commit/35b972dbc7d98c4363e658f1b6698161fa89f721))


## v0.1.0 (2025-07-05)

### Chores

* chore: consolidate to Ruff for all code quality tasks

- Remove isort dependency in favor of Ruff's import sorting
- Configure Ruff for formatting, linting, and import sorting
- Update documentation to reflect Ruff-first workflow
- Set changelog release date to 2025-07-06
- Apply Ruff formatting to existing code

This simplifies the development workflow to just two commands:
ruff format . && ruff check --fix .

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com> ([`bded59a`](https://github.com/astralblue/ign/commit/bded59ae0c731367aa014975926c21f71d4b9eb4))

* chore: consolidate dev dependencies into optional-dependencies

- Merge [dependency-groups] into [project.optional-dependencies]
- Add version constraints for black, isort, and ruff
- Remove duplicate PEP 735 section for broader compatibility
- Support both uv (--extra dev) and pip (.[dev]) workflows

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com> ([`0402bf6`](https://github.com/astralblue/ign/commit/0402bf67dbf4dca1acbb573670facc42c07bb762))

* chore: use uv ([`08ea680`](https://github.com/astralblue/ign/commit/08ea680e83546a8774b1ef34fbc2430f24ff9bdc))

* chore: sync .gitignore ([`3396ca2`](https://github.com/astralblue/ign/commit/3396ca2018a8cd4b5544edc0a34dbfedd23ce38b))

* chore: add project skeleton ([`751e14b`](https://github.com/astralblue/ign/commit/751e14bcda3b9b42ec64de5b35a4a2497fb84f61))

* chore: initial empty root-commit ([`5397eee`](https://github.com/astralblue/ign/commit/5397eee58554b957d4c5633f1a8dc0a8de785c24))

### Documentation

* docs: initial version ([`550a071`](https://github.com/astralblue/ign/commit/550a071891b9f745c5e7401eabce93d6fb2096a8))

### Features

* feat: rename project from gitig to ign

- Rename package directory from gitig/ to ign/
- Update all documentation and references
- Update project metadata in pyproject.toml
- Fix import statements throughout codebase
- Update IntelliJ IDEA configuration files
- Regenerate uv.lock with new package name

The name 'gitig' was already taken on PyPI, so renaming to 'ign'
(short for .gitignore) for publication.

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com> ([`26d0a95`](https://github.com/astralblue/ign/commit/26d0a95f1f19624ae5b8f794298be02e7b38b64c))

* feat: initial version ([`416de61`](https://github.com/astralblue/ign/commit/416de61964670b24573665e0281f1a72aa9dcf41))
