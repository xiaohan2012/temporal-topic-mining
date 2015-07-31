# coding: utf8

from util import load_line_corpus
from nose.tools import assert_equal


def test_load_line_corpus():
    corpus = load_line_corpus("test_data/line_corpus.dat")
    corpus = list(corpus)
    assert_equal(len(corpus), 3)
    assert_equal(corpus[0], u"We introduce the Randomized Dependence Coefficient (RDC), a measure of non-linear dependence between random variables of arbitrary dimension based on the Hirschfeld-Gebelein-RÃ©nyi Maximum Correlation Coefficient. RDC is defined in terms of correlation of random non-linear copula projections; it is invariant with respect to marginal distribution transformations, has low computational cost and is easy to implement: just five lines of R code, included at the end of the paper.")
