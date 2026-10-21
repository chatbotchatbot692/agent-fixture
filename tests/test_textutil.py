from textutil import slugify, truncate


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_truncate_short():
    assert truncate("abc", 5) == "abc"
