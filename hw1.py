"""
HW 1 SOLUTION

Please write all your code for HW 1 in this file and include this file
in your submission.
"""
from nltk.probability import FreqDist

""" Problem 1: Python Exercises """


def hello_world():
    print("Hello world!")


def foo_bar():
    print("foo bar")


def my_name():
    hello_world()
    print("My name is _.")  # Replace "_" with your name


def add_str(a: str, b: str) -> str:
    """Adds two numbers together"""
    return str(float(a) + float(b))


def swap_keys_values(d: dict) -> dict:
    """Problem 1e: Swaps the keys and values of a dict"""
    return {v: k for k, v in d.items()}


""" Problem 2: Identifying Keywords """


def joint_vocab(fd1: FreqDist, fd2: FreqDist) -> set[str]:
    """
    Problem 2c: Retrieves the joint vocabulary for two FreqDists.

    :return: The set of keys (token types) that appear in either fd1 or
        fd2
    """
    return set(fd1).union(fd2)


def smooth(fd: FreqDist, vocab: set[str], k: int = 1) -> FreqDist:
    """
    Problem 2c: Applies add-k smoothing to a FreqDist or a subset of a
    FreqDist.

    :param fd: A FreqDist containing token type counts for some corpus
    :param vocab: The set of token types that add-k smoothing will be
        applied to
    :param k: The counts for all token types in vocab (and no others)
        will be incremented by this number

    :return: A new FreqDist containing the smoothed version of fd
    """
    return fd + FreqDist({w: k for w in vocab})


def normalize(fd: FreqDist) -> FreqDist:
    """
    Problem 2d: Normalizes a FreqDist by the number of tokens in its
    originating corpus.

    :param fd: A FreqDist containing token type counts for some corpus

    :return: A FreqDist containing the proportion of tokens in fd's
        corpus matching each token type in fd
    """
    return FreqDist({w: c / fd.N() for w, c in fd.items()})


def freq_ratio(target_fd: FreqDist, ref_fd: FreqDist, k: int = 1) -> FreqDist:
    """
    Problem 2e: Calculates the frequency ratio between a target corpus
    and a reference corpus with add-k smoothing.

    :param target_fd: The token type counts for the target corpus
    :param ref_fd: The token type counts for the reference corpus
    :param k: The value of the "k" parameter for add-k smoothing

    :return: A FreqDist containing frequency ratios between target_fd
        and ref_fd, with add-k smoothing, for each token type appearing
        in either corpus
    """
    vocab = joint_vocab(target_fd, ref_fd)
    target_freqs = normalize(smooth(target_fd, vocab, k=k))
    ref_freqs = normalize(smooth(ref_fd, vocab, k=k))
    return FreqDist({w: target_freqs[w] / ref_freqs[w] for w in vocab})


def least_common(fd: FreqDist, n: int) -> list[tuple[str, int]]:
    """
    Problem 2g: Finds the n least common token types in a FreqDist.

    :return: The n items of fd with the lowest values, in ascending
        order, in the same format as fd.items()
    """
    return sorted(fd.items(), key=lambda x: x[1])[:n]
