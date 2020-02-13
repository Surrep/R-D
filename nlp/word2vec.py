import string
import numpy as np

from timeit import Timer
from collections import Counter

with open("./data/bible.txt") as fs:
    without_punctuation = str.maketrans('', '', string.punctuation)

    words = fs.read().lower().translate(without_punctuation).split()
    vocab = {k: v for v, k in enumerate(words)}

