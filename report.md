# ML Project Report
**Project** | **Details**
--------|--------
Date    | Mon, 18 Oct 2021 00:15:56 +0200 
Path    | `/home/bart/tudelft/thesis/mllint-example-projects`
Config  | `pyproject.toml`
Default | Yes
Git: Remote URL | `git@github.com:bvobart/mllint-example-projects.git`
Git: Commit     | `799d936bacdae8349d69db39fa080785bf0d96da`
Git: Branch     | `1-5-basic-fix-codestyle`
Git: Dirty Workspace?  | Yes
Number of Python files | 4
Lines of Python code   | 150

---

## Reports

### Version Control (`version-control`) — **100.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project uses Git | `version-control/code/git`
✅ | 100.0% | 1 | Project should not have any large files in its Git history | `version-control/code/git-no-big-files`
✅ | 100.0% | 1 | DVC: Project uses Data Version Control | `version-control/data/dvc`
✅ | 100.0% | 1 | DVC: Is installed | `version-control/data/dvc-is-installed`
✅ | 100.0% | 1 | DVC: Folder '.dvc' should be committed to Git | `version-control/data/commit-dvc-folder`
✅ | 100.0% | 1 | DVC: Should have at least one remote data storage configured | `version-control/data/dvc-has-remote`
✅ | 100.0% | 1 | DVC: Should be tracking at least one data file | `version-control/data/dvc-has-files`
 | _Total_ | | | 
✅ | **100.0**% | | Version Control | `version-control`

### Dependency Management (`dependency-management`) — **100.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project properly keeps track of its dependencies | `dependency-management/use`
✅ | 100.0% | 1 | Project should only use one dependency manager | `dependency-management/single`
✅ | 100.0% | 1 | Project places its development dependencies in dev-dependencies | `dependency-management/use-dev`
 | _Total_ | | | 
✅ | **100.0**% | | Dependency Management | `dependency-management`

### Code Quality (`code-quality`) — **62.5**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project should use code quality linters | `code-quality/use-linters`
✅ | 100.0% | 1 | All code quality linters should be installed in the current environment | `code-quality/linters-installed`
❌ | 0.0% | 1 | Pylint reports no issues with this project | `code-quality/pylint/no-issues`
✅ | 100.0% | 1 | Pylint is configured for this project | `code-quality/pylint/is-configured`
❌ | 0.0% | 1 | Mypy reports no issues with this project | `code-quality/mypy/no-issues`
✅ | 100.0% | 1 | Black reports no issues with this project | `code-quality/black/no-issues`
✅ | 100.0% | 1 | isort reports no issues with this project | `code-quality/isort/no-issues`
✅ | 100.0% | 0 | isort is properly configured | `code-quality/isort/is-configured`
❌ | 0.0% | 1 | Bandit reports no issues with this project | `code-quality/bandit/no-issues`
 | _Total_ | | | 
❌ | **62.5**% | | Code Quality | `code-quality`

#### Details — Project should use code quality linters — ✅

Hooray, all linters detected:

- Pylint
- Mypy
- Black
- isort
- Bandit


#### Details — Pylint reports no issues with this project — ❌

Pylint reported **17** issues with your project:

- `src/evaluate.py:1,0` - _(C0114)_ Missing module docstring
- `src/featurization.py:1,0` - _(C0114)_ Missing module docstring
- `src/featurization.py:29,0` - _(C0116)_ Missing function or method docstring
- `src/featurization.py:30,4` - _(C0103)_ Variable name "df" doesn't conform to snake_case naming style
- `src/featurization.py:35,0` - _(C0103)_ Argument name "df" doesn't conform to snake_case naming style
- `src/featurization.py:35,0` - _(C0116)_ Missing function or method docstring
- `src/featurization.py:44,31` - _(C0103)_ Variable name "fd" doesn't conform to snake_case naming style
- `src/featurization.py:46,4` - _(W0107)_ Unnecessary pass statement
- `src/prepare.py:1,0` - _(C0114)_ Missing module docstring
- `src/prepare.py:21,0` - _(W0622)_ Redefining built-in 'input'
- `src/prepare.py:26,0` - _(C0116)_ Missing function or method docstring
- `src/prepare.py:26,18` - _(W0621)_ Redefining name 'fd_in' from outer scope (line 48)
- `src/prepare.py:26,25` - _(W0621)_ Redefining name 'fd_out_train' from outer scope (line 49)
- `src/prepare.py:26,39` - _(W0621)_ Redefining name 'fd_out_test' from outer scope (line 50)
- `src/prepare.py:42,15` - _(W0703)_ Catching too general exception Exception
- `src/train.py:1,0` - _(C0114)_ Missing module docstring
- `src/train.py:16,0` - _(W0622)_ Redefining built-in 'input'


#### Details — Mypy reports no issues with this project — ❌

Mypy reported **22** issues with your project:

- `src/evaluate.py:6,1` - Error: Skipping analyzing 'sklearn.metrics': found module but no type hints or library stubs  [import]
- `src/evaluate.py:6,1` - Note: See https://mypy.readthedocs.io/en/latest/running_mypy.html#missing-imports
- `src/evaluate.py:6,1` - Error: Skipping analyzing 'sklearn': found module but no type hints or library stubs  [import]
- `src/evaluate.py:37,6` - Error: Incompatible types in assignment (expression has type "TextIO", variable has type "BinaryIO")  [assignment]
- `src/evaluate.py:38,59` - Error: Argument 2 to "dump" has incompatible type "BinaryIO"; expected "IO[str]"  [arg-type]
- `src/evaluate.py:40,6` - Error: Incompatible types in assignment (expression has type "TextIO", variable has type "BinaryIO")  [assignment]
- `src/evaluate.py:43,9` - Error: Argument 2 to "dump" has incompatible type "BinaryIO"; expected "IO[str]"  [arg-type]
- `src/evaluate.py:47,6` - Error: Incompatible types in assignment (expression has type "TextIO", variable has type "BinaryIO")  [assignment]
- `src/evaluate.py:49,107` - Error: Argument 2 to "dump" has incompatible type "BinaryIO"; expected "IO[str]"  [arg-type]
- `src/prepare.py:26,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/prepare.py:51,13` - Error: Call to untyped function "process_posts" in typed context  [no-untyped-call]
- `src/train.py:7,1` - Error: Skipping analyzing 'sklearn.ensemble': found module but no type hints or library stubs  [import]
- `src/featurization.py:6,1` - Error: Skipping analyzing 'pandas': found module but no type hints or library stubs  [import]
- `src/featurization.py:7,1` - Error: Skipping analyzing 'scipy.sparse': found module but no type hints or library stubs  [import]
- `src/featurization.py:7,1` - Error: Skipping analyzing 'scipy': found module but no type hints or library stubs  [import]
- `src/featurization.py:9,1` - Error: Skipping analyzing 'sklearn.feature_extraction.text': found module but no type hints or library stubs  [import]
- `src/featurization.py:29,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/featurization.py:35,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/featurization.py:52,12` - Error: Call to untyped function "get_df" in typed context  [no-untyped-call]
- `src/featurization.py:63,1` - Error: Call to untyped function "save_matrix" in typed context  [no-untyped-call]
- `src/featurization.py:66,11` - Error: Call to untyped function "get_df" in typed context  [no-untyped-call]
- `src/featurization.py:71,1` - Error: Call to untyped function "save_matrix" in typed context  [no-untyped-call]


#### Details — Black reports no issues with this project — ✅

Congratulations, Black is happy with your project!

#### Details — isort reports no issues with this project — ✅

Congratulations, `isort` is happy with your project!

#### Details — Bandit reports no issues with this project — ❌

Bandit reported **9** issues with your project:

- `src/evaluate.py:3` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/evaluate.py:20` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b301-pickle)
- `src/evaluate.py:23` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b301-pickle)
- `src/featurization.py:2` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/prepare.py:6` - _(B405, severity: LOW, confidence: HIGH)_ - Using xml.etree.ElementTree to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree with the equivalent defusedxml package, or make sure defusedxml.defuse_stdlib() is called. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b405-import-xml-etree)
- `src/prepare.py:30` - _(B311, severity: LOW, confidence: HIGH)_ - Standard pseudo-random generators are not suitable for security/cryptographic purposes. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b311-random)
- `src/prepare.py:31` - _(B314, severity: MEDIUM, confidence: HIGH)_ - Using xml.etree.ElementTree.fromstring to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.fromstring with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree)
- `src/train.py:2` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/train.py:23` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b301-pickle)


### Testing (`testing`) — **0.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 0.0% | 1 | Project has automated tests | `testing/has-tests`
❌ | 0.0% | 1 | Project passes all of its automated tests | `testing/pass`
❌ | 0.0% | 1 | Project provides a test coverage report | `testing/coverage`
❌ | 0.0% | 1 | Tests should be placed in the tests folder | `testing/tests-folder`
 | _Total_ | | | 
❌ | **0.0**% | | Testing | `testing`

#### Details — Project has automated tests — ❌

There are **0** test files in your project, but `mllint` was expecting at least **1**.

#### Details — Project passes all of its automated tests — ❌

No test report was provided.

Please update the `testing.report` setting in your project's `mllint` configuration to specify the path to your project's test report.

When using `pytest` to run your project's tests, use the `--junitxml=<filename>` option to generate such a test report, e.g.:
```sh
pytest --junitxml=tests-report.xml
```


#### Details — Project provides a test coverage report — ❌

No test coverage report was provided.

Please update the `testing.coverage.report` setting in your project's `mllint` configuration to specify the path to your project's test coverage report.

Generating a test coverage report with `pytest` can be done by adding and installing `pytest-cov` as a development dependency of your project. Then use the following command to run your tests and generate both a test report as well as a coverage report:
```sh
pytest --junitxml=tests-report.xml --cov=path_to_package_under_test --cov-report=xml
```


#### Details — Tests should be placed in the tests folder — ❌

Tip for when you start implementing tests: create a folder called `tests` at the root of your project and place all your Python test files in there, as per common convention.

### Continuous Integration (`ci`) — **0.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 0.0% | 1 | Project uses Continuous Integration (CI) | `ci/use`
 | _Total_ | | | 
❌ | **0.0**% | | Continuous Integration | `ci`

