"""
Tests the mlbasic.prepare module.
"""
from mlbasic.prepare import parse_post, process_post


def test_parse_post() -> None:
    "Tests the parse_post method"
    valid_xml = '<row Id="4186249" PostTypeId="1" AcceptedAnswerId="4186674" CreationDate="2010-11-15T16:06:29.293" Score="2" ViewCount="1246" Body="Loads of Text" OwnerUserId="207072" LastEditorUserId="207072" LastEditDate="2010-11-15T16:26:04.447" LastActivityDate="2010-11-15T17:08:56.730" Title="Searching and capturing a character using regular expressions Python" Tags="&lt;python&gt;&lt;regex&gt;&lt;search&gt;&lt;text-files&gt;" AnswerCount="3" CommentCount="0" />'  # pylint: disable=line-too-long
    post = parse_post(valid_xml, 0)
    assert post is not None
    assert isinstance(post, dict)
    assert post["Id"] == "4186249"
    assert post["AcceptedAnswerId"] == "4186674"
    assert post["Body"] == "Loads of Text"
    assert post["Title"] == "Searching and capturing a character using regular expressions Python"
    assert post["Tags"] == "<python><regex><search><text-files>"


def test_process_post() -> None:
    "Tests the process_post method"
    post = {
        "Id": "4186249",
        "Body": "Loads of Text",
        "Title": "Searching and capturing a character using regular expressions Python",
        "Tags": "<python><regex><search><text-files>",
    }
    csvline = process_post(post, "python")
    assert csvline == "4186249\t1\tSearching and capturing a character using regular expressions Python Loads of Text\n"
