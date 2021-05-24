# ML Project Report
Project | Details
--------|--------
Path    | `/home/bart/tudelft/thesis/mllint-example-projects`
Config  | `default`
Default | Yes
Date    | Mon, 24 May 2021 19:00:06 +0200 
Number of Python files | 4
Lines of Python code | 172

---

## Reports

### Version Control (`version-control`)

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project uses Git | `version-control/code/git`
✅ | 100.0% | 1 | Project should not use Git to track large files | `version-control/code/git-no-big-files`
✅ | 100.0% | 1 | DVC: Project uses Data Version Control | `version-control/data/dvc`
✅ | 100.0% | 1 | DVC: Is installed | `version-control/data/dvc-is-installed`
✅ | 100.0% | 1 | DVC: Folder '.dvc' should be committed to Git | `version-control/data/commit-dvc-folder`
✅ | 100.0% | 1 | DVC: Should have at least one remote data storage configured | `version-control/data/dvc-has-remote`
✅ | 100.0% | 1 | DVC: Should be tracking at least one data file | `version-control/data/dvc-has-files`

### Dependency Management (`dependency-management`)

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 20.0% | 1 | Project properly keeps track of its dependencies | `dependency-management/use`
✅ | 100.0% | 1 | Project should only use one dependency manager | `dependency-management/single`
❌ | 0.0% | 1 | Project places its development dependencies in dev-dependencies | `dependency-management/use-dev`

#### Details — Project properly keeps track of its dependencies — ❌

Your project seems to be managing its dependencies using a `requirements.txt` file.
Such `requirements.txt` files have a high tendency to include unrelated packages or packages that cannot be resolved from [PyPI](https://pypi.org/) (Pip's standard package index),
are hard to maintain as they have no distinction between run-time dependencies and development-time dependencies, nor direct and indirect dependencies,
and may hamper the reproducibility of your ML project by underspecifying their exact versions and checksums.

We therefore recommend switching to Poetry or Pipenv and keeping track of all your dependencies there.

#### Details — Project places its development dependencies in dev-dependencies — ❌

Your project's main dependency manager is a `requirements.txt` file, which doesn't distinguish between regular dependencies and development dependencies.

### Code Quality (`code-quality`)

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 0.0% | 1 | Project should use code quality linters | `code-quality/use-linters`
✅ | 100.0% | 1 | All code quality linters should be installed in the current environment | `code-quality/linters-installed`
❌ | 0.0% | 1 | Pylint reports no issues with this project | `code-quality/pylint/no-issues`
❌ | 0.0% | 1 | Pylint is configured for this project | `code-quality/pylint/is-configured`
❌ | 0.0% | 1 | Mypy reports no issues with this project | `code-quality/mypy/no-issues`
❌ | 0.0% | 1 | Black reports no issues with this project | `code-quality/black/no-issues`
❌ | 0.0% | 1 | isort reports no issues with this project | `code-quality/isort/no-issues`
❌ | 0.0% | 0 | isort is properly configured | `code-quality/isort/is-configured`
❌ | 0.0% | 1 | Bandit reports no issues with this project | `code-quality/bandit/no-issues`

#### Details — Project should use code quality linters — ❌

Oh my, no code quality linters were detected in your project!

We recommend that you start using the following linters in your project to help you measure and maintain the quality of your code:

- Pylint
- Mypy
- Black
- isort
- Bandit


This rule will be satisfied, iff for each of these linters:
- **Either** there is a configuration file for this linter in the project
- **Or** the linter is a dependency of the project

Specifically, we recommend adding each linter to the development dependencies of your dependency manager,
e.g. using `poetry add --dev pylint` or `pipenv install --dev pylint`


#### Details — Pylint reports no issues with this project — ❌

Pylint reported **24** issues with your project:

- `src/evaluate.py:1,0` - _(C0114)_ Missing module docstring
- `src/evaluate.py:6,0` - _(E0401)_ Unable to import 'sklearn.metrics'
- `src/featurization.py:1,0` - _(C0114)_ Missing module docstring
- `src/featurization.py:3,0` - _(E0401)_ Unable to import 'pandas'
- `src/featurization.py:6,0` - _(E0401)_ Unable to import 'scipy.sparse'
- `src/featurization.py:9,0` - _(E0401)_ Unable to import 'sklearn.feature_extraction.text'
- `src/featurization.py:10,0` - _(E0401)_ Unable to import 'sklearn.feature_extraction.text'
- `src/featurization.py:32,0` - _(C0116)_ Missing function or method docstring
- `src/featurization.py:33,4` - _(C0103)_ Variable name "df" doesn't conform to snake_case naming style
- `src/featurization.py:44,0` - _(C0103)_ Argument name "df" doesn't conform to snake_case naming style
- `src/featurization.py:44,0` - _(C0116)_ Missing function or method docstring
- `src/featurization.py:53,31` - _(C0103)_ Variable name "fd" doesn't conform to snake_case naming style
- `src/featurization.py:55,4` - _(W0107)_ Unnecessary pass statement
- `src/featurization.py:5,0` - _(C0411)_ standard import "import pickle" should be placed before "import pandas as pd"
- `src/prepare.py:1,0` - _(C0114)_ Missing module docstring
- `src/prepare.py:20,0` - _(W0622)_ Redefining built-in 'input'
- `src/prepare.py:25,0` - _(C0116)_ Missing function or method docstring
- `src/prepare.py:25,18` - _(W0621)_ Redefining name 'fd_in' from outer scope (line 47)
- `src/prepare.py:25,25` - _(W0621)_ Redefining name 'fd_out_train' from outer scope (line 48)
- `src/prepare.py:25,39` - _(W0621)_ Redefining name 'fd_out_test' from outer scope (line 49)
- `src/prepare.py:41,15` - _(W0703)_ Catching too general exception Exception
- `src/train.py:1,0` - _(C0114)_ Missing module docstring
- `src/train.py:15,0` - _(W0622)_ Redefining built-in 'input'
- `src/train.py:6,0` - _(E0401)_ Unable to import 'sklearn.ensemble'


#### Details — Mypy reports no issues with this project — ❌

Mypy reported **24** issues with your project:

- `src/evaluate.py:6,1` - Error: Cannot find implementation or library stub for module named 'sklearn.metrics'  [import]
- `src/evaluate.py:6,1` - Note: See https://mypy.readthedocs.io/en/latest/running_mypy.html#missing-imports
- `src/evaluate.py:6,1` - Error: Cannot find implementation or library stub for module named 'sklearn'  [import]
- `src/evaluate.py:37,6` - Error: Incompatible types in assignment (expression has type "TextIO", variable has type "BinaryIO")  [assignment]
- `src/evaluate.py:38,59` - Error: Argument 2 to "dump" has incompatible type "BinaryIO"; expected "IO[str]"  [arg-type]
- `src/evaluate.py:40,6` - Error: Incompatible types in assignment (expression has type "TextIO", variable has type "BinaryIO")  [assignment]
- `src/evaluate.py:46,9` - Error: Argument 2 to "dump" has incompatible type "BinaryIO"; expected "IO[str]"  [arg-type]
- `src/evaluate.py:48,6` - Error: Incompatible types in assignment (expression has type "TextIO", variable has type "BinaryIO")  [assignment]
- `src/evaluate.py:54,9` - Error: Argument 2 to "dump" has incompatible type "BinaryIO"; expected "IO[str]"  [arg-type]
- `src/train.py:4,1` - Error: Skipping analyzing 'numpy': found module but no type hints or library stubs  [import]
- `src/train.py:6,1` - Error: Cannot find implementation or library stub for module named 'sklearn.ensemble'  [import]
- `src/prepare.py:25,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/prepare.py:50,13` - Error: Call to untyped function "process_posts" in typed context  [no-untyped-call]
- `src/featurization.py:3,1` - Error: Cannot find implementation or library stub for module named 'pandas'  [import]
- `src/featurization.py:4,1` - Error: Skipping analyzing 'numpy': found module but no type hints or library stubs  [import]
- `src/featurization.py:6,1` - Error: Cannot find implementation or library stub for module named 'scipy.sparse'  [import]
- `src/featurization.py:6,1` - Error: Cannot find implementation or library stub for module named 'scipy'  [import]
- `src/featurization.py:9,1` - Error: Cannot find implementation or library stub for module named 'sklearn.feature_extraction.text'  [import]
- `src/featurization.py:32,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/featurization.py:44,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/featurization.py:61,12` - Error: Call to untyped function "get_df" in typed context  [no-untyped-call]
- `src/featurization.py:76,1` - Error: Call to untyped function "save_matrix" in typed context  [no-untyped-call]
- `src/featurization.py:79,11` - Error: Call to untyped function "get_df" in typed context  [no-untyped-call]
- `src/featurization.py:84,1` - Error: Call to untyped function "save_matrix" in typed context  [no-untyped-call]


#### Details — Black reports no issues with this project — ❌

Black reported **4** files in your project that it would reformat:

- `src/evaluate.py`
- `src/train.py`
- `src/prepare.py`
- `src/featurization.py`

Black can fix these issues automatically when you run `black .` in your project.

#### Details — isort reports no issues with this project — ❌

isort reported **4** files in your project that it would fix:

- `src/evaluate.py` - Imports are incorrectly sorted and/or formatted.
- `src/train.py` - Imports are incorrectly sorted and/or formatted.
- `src/prepare.py` - Imports are incorrectly sorted and/or formatted.
- `src/featurization.py` - Imports are incorrectly sorted and/or formatted.

isort can fix these issues automatically when you run `isort .` in your project.

#### Details — isort is properly configured — ❌

isort is not properly configured.
In order to be compatible with [Black](https://github.com/psf/black), which mllint also recommends using,
you should configure `isort` to use the `black` profile.
Furthermore, we recommend centralising your configuration in your `pyproject.toml`

Thus, ensure that your `pyproject.toml` contains at least the following section:

```toml
[tool.isort]
profile = "black"
```


#### Details — Bandit reports no issues with this project — ❌

Bandit reported **9** issues with your project:

- `src/evaluate.py:3` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/evaluate.py:20` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b301-pickle)
- `src/evaluate.py:23` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b301-pickle)
- `src/featurization.py:5` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/prepare.py:3` - _(B405, severity: LOW, confidence: HIGH)_ - Using xml.etree.ElementTree to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree with the equivalent defusedxml package, or make sure defusedxml.defuse_stdlib() is called. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b405-import-xml-etree)
- `src/prepare.py:29` - _(B311, severity: LOW, confidence: HIGH)_ - Standard pseudo-random generators are not suitable for security/cryptographic purposes. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b311-random)
- `src/prepare.py:30` - _(B314, severity: MEDIUM, confidence: HIGH)_ - Using xml.etree.ElementTree.fromstring to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.fromstring with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree)
- `src/train.py:3` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/train.py:22` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b301-pickle)


### Continuous Integration (`ci`)

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 0.0% | 1 | Project uses Continuous Integration (CI) | `ci/use`

