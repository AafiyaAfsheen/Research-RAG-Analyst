from difflib import SequenceMatcher


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


def filter_context(chunks, threshold=0.7):

    filtered = []

    for chunk in chunks:

        duplicate = False

        for existing in filtered:

            if similarity(chunk["text"], existing["text"]) > threshold:
                duplicate = True
                break

        if not duplicate:
            filtered.append(chunk)

    return filtered