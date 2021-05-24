# ML Project Report
Project | Details
--------|--------
Path    | `/home/bart/tudelft/thesis/mllint-example-projects`
Config  | `pyproject.toml`
Default | Yes
Date    | Mon, 24 May 2021 22:27:16 +0200 
Number of Python files | 4
Lines of Python code | 162

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
✅ | 100.0% | 1 | Project properly keeps track of its dependencies | `dependency-management/use`
✅ | 100.0% | 1 | Project should only use one dependency manager | `dependency-management/single`
✅ | 100.0% | 1 | Project places its development dependencies in dev-dependencies | `dependency-management/use-dev`

### Code Quality (`code-quality`)

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project should use code quality linters | `code-quality/use-linters`
✅ | 100.0% | 1 | All code quality linters should be installed in the current environment | `code-quality/linters-installed`
✅ | 100.0% | 1 | Pylint reports no issues with this project | `code-quality/pylint/no-issues`
✅ | 100.0% | 1 | Pylint is configured for this project | `code-quality/pylint/is-configured`
❌ | 0.0% | 1 | Mypy reports no issues with this project | `code-quality/mypy/no-issues`
✅ | 100.0% | 1 | Black reports no issues with this project | `code-quality/black/no-issues`
✅ | 100.0% | 1 | isort reports no issues with this project | `code-quality/isort/no-issues`
✅ | 100.0% | 0 | isort is properly configured | `code-quality/isort/is-configured`
❌ | 0.0% | 1 | Bandit reports no issues with this project | `code-quality/bandit/no-issues`

#### Details — Project should use code quality linters — ✅

Hooray, all linters detected:

- Bandit
- Pylint
- Mypy
- Black
- isort


#### Details — Pylint reports no issues with this project — ✅

Congratulations, Pylint is happy with your project!

#### Details — Mypy reports no issues with this project — ❌

Mypy reported **22** issues with your project:

- `src/evaluate.py:11,1` - Error: Skipping analyzing 'sklearn.metrics': found module but no type hints or library stubs  [import]
- `src/evaluate.py:11,1` - Note: See https://mypy.readthedocs.io/en/latest/running_mypy.html#missing-imports
- `src/evaluate.py:11,1` - Error: Skipping analyzing 'sklearn': found module but no type hints or library stubs  [import]
- `src/evaluate.py:42,6` - Error: Incompatible types in assignment (expression has type "TextIO", variable has type "BinaryIO")  [assignment]
- `src/evaluate.py:43,59` - Error: Argument 2 to "dump" has incompatible type "BinaryIO"; expected "IO[str]"  [arg-type]
- `src/evaluate.py:45,6` - Error: Incompatible types in assignment (expression has type "TextIO", variable has type "BinaryIO")  [assignment]
- `src/evaluate.py:48,9` - Error: Argument 2 to "dump" has incompatible type "BinaryIO"; expected "IO[str]"  [arg-type]
- `src/evaluate.py:52,6` - Error: Incompatible types in assignment (expression has type "TextIO", variable has type "BinaryIO")  [assignment]
- `src/evaluate.py:54,107` - Error: Argument 2 to "dump" has incompatible type "BinaryIO"; expected "IO[str]"  [arg-type]
- `src/train.py:13,1` - Error: Skipping analyzing 'sklearn.ensemble': found module but no type hints or library stubs  [import]
- `src/prepare.py:43,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/prepare.py:78,13` - Error: Call to untyped function "process_posts" in typed context  [no-untyped-call]
- `src/featurization.py:11,1` - Error: Skipping analyzing 'pandas': found module but no type hints or library stubs  [import]
- `src/featurization.py:12,1` - Error: Skipping analyzing 'scipy.sparse': found module but no type hints or library stubs  [import]
- `src/featurization.py:12,1` - Error: Skipping analyzing 'scipy': found module but no type hints or library stubs  [import]
- `src/featurization.py:14,1` - Error: Skipping analyzing 'sklearn.feature_extraction.text': found module but no type hints or library stubs  [import]
- `src/featurization.py:34,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/featurization.py:43,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/featurization.py:62,14` - Error: Call to untyped function "parse_input_tsv" in typed context  [no-untyped-call]
- `src/featurization.py:73,1` - Error: Call to untyped function "save_matrix" in typed context  [no-untyped-call]
- `src/featurization.py:76,13` - Error: Call to untyped function "parse_input_tsv" in typed context  [no-untyped-call]
- `src/featurization.py:81,1` - Error: Call to untyped function "save_matrix" in typed context  [no-untyped-call]


#### Details — Black reports no issues with this project — ✅

Congratulations, Black is happy with your project!

#### Details — isort reports no issues with this project — ✅

Congratulations, `isort` is happy with your project!

#### Details — Bandit reports no issues with this project — ❌

Bandit reported **9** issues with your project:

- `src/evaluate.py:8` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/evaluate.py:25` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b301-pickle)
- `src/evaluate.py:28` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b301-pickle)
- `src/featurization.py:7` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/prepare.py:13` - _(B405, severity: LOW, confidence: HIGH)_ - Using xml.etree.ElementTree to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree with the equivalent defusedxml package, or make sure defusedxml.defuse_stdlib() is called. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b405-import-xml-etree)
- `src/prepare.py:37` - _(B314, severity: MEDIUM, confidence: HIGH)_ - Using xml.etree.ElementTree.fromstring to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.fromstring with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree)
- `src/prepare.py:62` - _(B311, severity: LOW, confidence: HIGH)_ - Standard pseudo-random generators are not suitable for security/cryptographic purposes. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b311-random)
- `src/train.py:8` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/train.py:29` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b301-pickle)


### Continuous Integration (`ci`)

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 0.0% | 1 | Project uses Continuous Integration (CI) | `ci/use`

