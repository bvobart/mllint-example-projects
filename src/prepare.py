"""
Module prepare.py is reponsible for preparing the dataset for featurization.
It parses each line of the file provided as its argument for XML data about StackOverflow posts
and prepares it for feature extraction by converting the data to TSV format and splitting into train and test set,
which it outputs to `./data/prepared/{train,test}.tsv`
"""

import io
import os
import random
import re
import sys
from typing import IO, Optional, cast

import defusedxml.ElementTree
import yaml

params = yaml.safe_load(open("params.yaml"))["prepare"]

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython prepare.py data-file\n")
    sys.exit(1)

# Test data set split ratio
split = params["split"]
random.seed(params["seed"])

input_file = sys.argv[1]
output_train_path = os.path.join("data", "prepared", "train.tsv")
output_test_path = os.path.join("data", "prepared", "test.tsv")


def parse_post(line: str, line_no: int) -> Optional[dict[str, str]]:
    "Parses a raw line of XML post data into XML attributes, returning None on error."
    try:
        return cast(dict[str, str], defusedxml.ElementTree.fromstring(line).attrib)
    except defusedxml.ElementTree.ParseError as parse_ex:
        sys.stderr.write(f"XML parsing error at line {line_no}: {parse_ex}\n")
        return None


def process_posts(xml_data: IO[str], output_train: IO[str], output_test: IO[str], target_tag: str) -> None:
    """
    Parses the StackOverflow posts from the `xml_data` and labels with a 1 if the post has the `target_tag` on it,
    0 otherwise. Then saves the post's ID, title, text and label to `output_train` and `output_test`,
    depending on the split ratio from params.
    """
    num = 1
    for line in xml_data:
        try:
            attr = parse_post(line, num)
            if attr is None:
                continue

            pid = attr.get("Id", "")
            label = 1 if target_tag in attr.get("Tags", "") else 0
            title = re.sub(r"\s+", " ", attr.get("Title", "")).strip()
            body = re.sub(r"\s+", " ", attr.get("Body", "")).strip()
            text = title + " " + body

            fd_out = output_train if random.random() > split else output_test
            fd_out.write("{}\t{}\t{}\n".format(pid, label, text))

            num += 1
        except re.error as regex_err:
            sys.stderr.write(f"Error transforming XML properties of line {num}: {regex_err}\n")
        except Exception as ex:
            sys.stderr.write(f"Fatal error analysing line {num}: {ex}\n")
            raise ex


os.makedirs(os.path.join("data", "prepared"), exist_ok=True)

with io.open(input_file, encoding="utf8") as fd_in:
    with io.open(output_train_path, "w", encoding="utf8") as fd_out_train:
        with io.open(output_test_path, "w", encoding="utf8") as fd_out_test:
            process_posts(fd_in, fd_out_train, fd_out_test, "<python>")
