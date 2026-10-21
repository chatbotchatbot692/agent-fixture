"""Small text helpers."""


def slugify(text):
    """Lowercase, replace runs of non-alphanumerics with a single dash."""
    out = []
    in_run = False
    for ch in text.lower():
        if ch.isalnum():
            out.append(ch)
            in_run = False
        elif not in_run:
            out.append("-")
            in_run = True
    return "".join(out).strip("-")


def truncate(text, n):
    """Return text cut to n chars, adding '...' when cut (total length <= n)."""
    if n <= 0:
        return ""
    if len(text) <= n:
        return text
    if n < len("..."):
        # Not enough room for the ellipsis, so just cut the text.
        return text[:n]
    return text[: n - len("...")] + "..."
