## v1.8.14 - 2024-12-14
## v1.8.14

### Internal Changes

- Improved the GitHub Actions workflow for version increments:
  - The changelog entry is now written to a temporary file before being appended to the existing `CHANGELOG.md`, ensuring a cleaner update process.
  - Enhanced the method for setting the output of the changelog entry in the workflow, replacing the deprecated `set-output` command with a more robust approach.
- Updated the `generate_changelog.py` script to ensure the changelog entry generation process adheres to the latest guidelines, specifically excluding dates and release status from entries.

## v1.8.12 - 2024-12-14
# Changelog

## v1.8.12 - 2023-10-XX

### Internal Changes

- Updated the version increment workflow to simplify the condition for updating `CHANGELOG.md`. The check for non-empty `diff` output has been removed, and now it only checks if `env.new_version` is not empty. This change streamlines the workflow process for updating the changelog.

## v1.8.13 - 2024-12-14
# Changelog

## v1.8.13 - 2023-10-XX

### Internal Changes

- Enhanced the GitHub Actions workflow for version increments. The process now includes reading the changelog entry from a file and using it as the body of the release notes. This improvement ensures that the release notes are automatically populated with the latest changelog entry.
- Re-enabled the steps for creating a new GitHub release and triggering the release workflow. The workflow now checks if `env.new_version` is not empty before proceeding, improving the automation of the release process.

