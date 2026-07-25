# Python 3.10 Minimum Version Design

## Goal

Align the package metadata, documentation, automation runtimes, and dependency
policy around Python 3.10 as the minimum supported version.

## Changes

- Declare `python_requires=">=3.10"` in `setup.py` so installers reject
  unsupported interpreters.
- Update the quickstart prerequisite from Python 3.8+ to Python 3.10+.
- Run the publishing and version-increment workflows on Python 3.10 instead of
  the unsupported Python 3.9 runtime.
- Add a focused regression test that executes `setup.py` with a captured
  `setuptools.setup` call and verifies the declared minimum.

## Verification

- Demonstrate the new metadata test fails before changing `setup.py`, then
  passes afterward.
- Run the focused metadata test and package build/metadata inspection.
- Install the combined dependency set under Python 3.10 and run the full test
  suite, reporting any pre-existing failures rather than hiding them.

## Delivery

Push the verified change to the repository's default `master` branch. Re-fetch
pull requests #2020 and #2023, verify their recorded head SHAs, and merge them
through GitHub using expected-head guards. Finally, synchronize the local
`master` branch with `origin/master`.
