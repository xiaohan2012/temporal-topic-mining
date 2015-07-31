import codecs


def load_line_corpus(path):
    with codecs.open(path, "r", "utf8") as f:
        for l in f:
            yield l.strip()
