from textutil import slugify, truncate


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_repeated_and_trailing_dashes():
    assert slugify("Hello,  World!") == "hello-world"


def test_slugify_leading_trailing_non_alnum():
    assert slugify("--foo--bar--") == "foo-bar"


def test_truncate_short():
    assert truncate("abc", 5) == "abc"


def test_truncate_exact_length():
    assert truncate("abcdefghij", 6) == "abc..."


def test_truncate_very_short_n():
    assert truncate("abcdef", 2) == "ab"
