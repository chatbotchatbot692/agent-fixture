"""Small text helpers."""


def slugify(text):
    """Lowercase, replace runs of non-alphanumerics with a single dash."""
    out = []
    for ch in text.lower():
        out.append(ch if ch.isalnum() else "-")
    return "".join(out)


def truncate(text, n):
    """Return text cut to n chars, adding '...' when cut (total length <= n)."""
    if len(text) <= n:
        return text
    return text[:n] + "..."
