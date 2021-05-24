"""
Module train.py is responsible for actually training the model using a RandomForestClassifier
with params from the params.yaml file.
Will dump the output RandomForestClassifier object to the given model file.
"""

import os
import pickle
import sys

import numpy as np
import yaml
from sklearn.ensemble import RandomForestClassifier

params = yaml.safe_load(open("params.yaml"))["train"]

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython train.py features model\n")
    sys.exit(1)

features_dir = sys.argv[1]
model_file = sys.argv[2]
seed = params["seed"]
n_est = params["n_est"]
min_split = params["min_split"]

with open(os.path.join(features_dir, "train.pkl"), "rb") as fd:
    matrix = pickle.load(fd)

labels = np.squeeze(matrix[:, 1].toarray())
x = matrix[:, 2:]

sys.stderr.write("Input matrix size {}\n".format(matrix.shape))
sys.stderr.write("X matrix size {}\n".format(x.shape))
sys.stderr.write("Y matrix size {}\n".format(labels.shape))

clf = RandomForestClassifier(n_estimators=n_est, min_samples_split=min_split, n_jobs=2, random_state=seed)

clf.fit(x, labels)

with open(model_file, "wb") as fd:
    pickle.dump(clf, fd)
