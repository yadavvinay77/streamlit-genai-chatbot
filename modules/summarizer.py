def summarize_text(text, max_len=400):
    """
    Truncate or return text up to max_len characters.
    """
    if len(text) <= max_len:
        return text
    return text[:max_len].rsplit(" ", 1)[0] + "..."
