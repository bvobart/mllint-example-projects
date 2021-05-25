# `mllint` - Example Projects

This repository contains a set of example projects for [`mllint`](https://github.com/bvobart/mllint), the command-line utility to evaluate the quality of Machine Learning (ML) projects by means of static analysis of the project's repository.

Each branch of this repository, except `main`, implements a ML project written in Python that has used `mllint` to generate a project quality report (see `report.md`)

> _Note: it is usually not recommended to commit `mllint` reports to the project repository, similar to how code coverage reports should also not be committed to the repository. This is only done in this repository for demo purposes._

## Projects

### Basic

The branches `1-*-basic*` implement a basic ML project, that starts out with a `requirements.txt` to track Python dependencies, no code or data quality linting and no data versioning or CI. `mllint` therefore also gives this version of the project very poor scores. Over the course of several iterations, we implement several improvements in the project, guided by `mllint`'s recommendations. A description of these improvements, along with the branch of this repository that stores this iteration, can be found in the table below.

\# | Branch | Improvements relative to previous iteration
---|--------|------------------------------------------------
1 | [`1-1-basic`](https://github.com/bvobart/mllint-example-projects/tree/1-1-basic) | -
2 | [`1-2-basic-dvc`](https://github.com/bvobart/mllint-example-projects/tree/1-2-basic-dvc) | Use Data Version Control (DVC) to track data dependencies, instead of downloading from Drive folder with a `data/get_data.py` script.
3 | [`1-3-basic-poetry`](https://github.com/bvobart/mllint-example-projects/tree/1-3-basic-poetry) | Start using Poetry
4 | [`1-4-basic-linting`](https://github.com/bvobart/mllint-example-projects/tree/1-4-basic-linting) | Add Pylint, Mypy, Black, isort and Bandit to dev dependencies, create configurations for Pylint and isort
5 | [`1-5-basic-fix-codestyle`](https://github.com/bvobart/mllint-example-projects/tree/1-5-basic-fix-codestyle) | Run `black .` and `isort .` to fix code style issues
6 | [`1-6-basic-fix-pylint`](https://github.com/bvobart/mllint-example-projects/tree/1-6-basic-pylint) | Fix all Pylint's code quality issues
7 | [`1-7-basic-fix-bandit`](https://github.com/bvobart/mllint-example-projects/tree/1-7-basic-bandit) | Fix all Bandit's security issues
8 | [`1-8-basic-fix-mypy`](https://github.com/bvobart/mllint-example-projects/tree/1-8-basic-mypy) | Fix all Mypy's type-checking issues.
9 | [`1-9-basic-fix-ci`](https://github.com/bvobart/mllint-example-projects/tree/1-9-basic-ci) | Implement a basic CI pipeline to install the project's dependencies and run `mllint` on it, saving the report it generates as a pipeline artifact (e.g. [this artifact](https://github.com/bvobart/mllint-example-projects/suites/2828997561/artifacts/63048199)).

> _Based on the [DVC Get Started](https://github.com/iterative/example-get-started) project from the creators of [Data Version Control (DVC)](https://github.com/iterative/dvc)_
