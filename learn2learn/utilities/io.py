import string


def load_corpus(path):
    with open(path) as fs:
        no_punctuation = str.maketrans('', '', string.punctuation)
        corpus = fs.read().lower().translate(no_punctuation).split()

    return corpus


def make_vocab(corpus):
    vocab = {}
    identity = 0

    for word in corpus:
        if word not in vocab:
            vocab[word] = identity
            identity += 1

    return vocab
