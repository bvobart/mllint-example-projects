# `mllint` - Example Projects

This repository contains a set of example projects for [`mllint`](https://github.com/bvobart/mllint), the command-line utility to evaluate the quality of Machine Learning (ML) projects by means of static analysis of the project's repository.

## Current Project: Basic

This branch implements a basic ML project with a `requirements.txt` to track Python dependencies, no code or data quality linting and no data versioning or CI.

To view `mllint`'s report for this project, see [report.md](report.md)

To run this project, run the following commands in order:
```sh
# Install dependencies in a virtualenv
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Download the dataset
dvc pull

# Runs the scripts to prepare the training data, featurize it, train the model and evaluate it.
python src/prepare.py data/data.xml
python src/featurization.py data/prepared data/features
python src/train.py data/features model.pkl
python src/evaluate.py model.pkl data/features scores.json prc.json roc.json
```

> _Based on the [DVC Get Started](https://github.com/iterative/example-get-started) project from the creators of [Data Version Control (DVC)](https://github.com/iterative/dvc)_
