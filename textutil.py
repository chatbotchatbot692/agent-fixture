"""Small text helpers."""


def slugify(text):
    """Lowercase, replace runs of non-alphanumerics with a single dash."""
    out = []
    prev_dash = False
    for ch in text.lower():
        if ch.isalnum():
            out.append(ch)
            prev_dash = False
        elif not prev_dash:
            out.append("-")
            prev_dash = True
    result = "".join(out)
    return result.strip("-")


def truncate(text, n):
    """Return text cut to n chars, adding '...' when cut (total length <= n)."""
    if len(text) <= n:
        return text
    if n <= 3:
        return text[:n]
    return text[:n - 3] + "..."
