"""
Module featurization.py is responsible for taking the train and test TSV files
and generating their feature matrices using count vectorisation and tf-idf transformation.
"""

import os
import pickle
import sys

import numpy as np
import pandas as pd
import scipy.sparse as sparse
import yaml
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

params = yaml.safe_load(open("params.yaml"))["featurize"]

np.set_printoptions(suppress=True)

if len(sys.argv) != 3 and len(sys.argv) != 5:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython featurization.py data-dir-path features-dir-path\n")
    sys.exit(1)

train_input = os.path.join(sys.argv[1], "train.tsv")
test_input = os.path.join(sys.argv[1], "test.tsv")
train_output = os.path.join(sys.argv[2], "train.pkl")
test_output = os.path.join(sys.argv[2], "test.pkl")

max_features = params["max_features"]
ngrams = params["ngrams"]


def parse_input_tsv(input_file: str) -> pd.DataFrame:
    """
    This function reads the given TSV input file and returns its contents as a Pandas DataFrame.
    """
    data = pd.read_csv(input_file, encoding="utf-8", header=None, delimiter="\t", names=["id", "label", "text"])
    sys.stderr.write(f"The input data frame {data} size is {data.shape}\n")
    return data


def save_matrix(data: pd.DataFrame, matrix: sparse.csr_matrix, output: str) -> None:
    """
    This function saves a csr_matrix output by a TfidfTransformer.transform() to an output file as a Pickle.
    """
    id_matrix = sparse.csr_matrix(data.id.astype(np.int64)).T
    label_matrix = sparse.csr_matrix(data.label.astype(np.int64)).T

    result = sparse.hstack([id_matrix, label_matrix, matrix], format="csr")

    msg = "The output matrix {} size is {} and data type is {}\n"
    sys.stderr.write(msg.format(output, result.shape, result.dtype))

    with open(output, "wb") as output_file:
        pickle.dump(result, output_file, pickle.HIGHEST_PROTOCOL)


os.makedirs(sys.argv[2], exist_ok=True)

# Generate train feature matrix
data_train = parse_input_tsv(train_input)
train_words = np.array(data_train.text.str.lower().values.astype("U"))

bag_of_words = CountVectorizer(stop_words="english", max_features=max_features, ngram_range=(1, ngrams))

bag_of_words.fit(train_words)
train_words_binary_matrix = bag_of_words.transform(train_words)
tfidf = TfidfTransformer(smooth_idf=False)
tfidf.fit(train_words_binary_matrix)
train_words_tfidf_matrix = tfidf.transform(train_words_binary_matrix)

save_matrix(data_train, train_words_tfidf_matrix, train_output)

# Generate test feature matrix
data_test = parse_input_tsv(test_input)
test_words = np.array(data_test.text.str.lower().values.astype("U"))
test_words_binary_matrix = bag_of_words.transform(test_words)
test_words_tfidf_matrix = tfidf.transform(test_words_binary_matrix)

save_matrix(data_test, test_words_tfidf_matrix, test_output)
