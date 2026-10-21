from textutil import slugify, truncate


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_truncate_short():
    assert truncate("abc", 5) == "abc"


def test_slugify_collapses_repeated_dashes():
    assert slugify("Hello,  World!") == "hello-world"


def test_slugify_collapses_runs_of_non_alphanumerics():
    assert slugify("a---b") == "a-b"
    assert slugify("a___b") == "a-b"
    assert slugify("a - _ b") == "a-b"


def test_slugify_strips_leading_and_trailing_dashes():
    assert slugify("!Hello!") == "hello"
    assert slugify("  spaced  ") == "spaced"
    assert slugify("...") == ""
    assert slugify("") == ""


def test_slugify_keeps_alphanumerics_only():
    assert slugify("Hello World") == "hello-world"
    assert slugify("abc123") == "abc123"


def test_truncate_counts_ellipsis_towards_limit():
    assert truncate("abcdefghij", 6) == "abc..."
    assert len(truncate("abcdefghij", 6)) == 6


def test_truncate_total_length_never_exceeds_n():
    text = "abcdefghij"
    for n in range(0, 15):
        assert len(truncate(text, n)) <= n


def test_truncate_exact_length_is_unchanged():
    assert truncate("abc", 3) == "abc"
    assert truncate("abc", 0) == ""


def test_truncate_too_small_for_ellipsis():
    assert truncate("abcdefghij", 2) == "ab"
    assert truncate("abcdefghij", 1) == "a"
    assert truncate("abcdefghij", 0) == ""


def test_truncate_ellipsis_only_when_it_fits():
    assert truncate("abcdefghij", 3) == "..."
