# coding: utf-8

from nose.tools import assert_equals
from http_util import (download_jmlr_abstract,
                       extract_page_urls,
                       extract_content)


def test_download_jmlr_abstract():
    url = "http://jmlr.org/proceedings/papers/v32/samdani14.html"
    actual = download_jmlr_abstract(url)
    expected = """This paper presents a latent variable structured prediction model for discriminative supervised clustering of items called the Latent Left-linking Model (L3M). We present an online clustering algorithm for L3M based on a feature-based item similarity function. We provide a learning framework for estimating the similarity function and present a fast stochastic gradient-based learning technique. In our experiments on coreference resolution and document clustering, L3 M outperforms several existing online as well as batch supervised clustering techniques."""

    assert_equals(actual, expected)


def test_extract_page_urls():
    page_url = "http://papers.nips.cc/book/advances-in-neural-information-processing-systems-26-2013"
    link_parent_selector = "div.main ul li"
    link_selector = "a:eq(0)"

    urls = list(extract_page_urls(page_url,
                                   link_parent_selector,
                                   link_selector))
    actual = len(urls)
    expected = 360

    assert_equals(actual, expected)


def test_extract_content():
    url = "http://papers.nips.cc/paper/5138-the-randomized-dependence-coefficient"
    content_selector = "div.main p.abstract"

    actual = extract_content(url, content_selector).strip()
    expected = u"""We introduce the Randomized Dependence Coefficient (RDC), a measure of non-linear dependence between random variables of arbitrary dimension based on the Hirschfeld-Gebelein-Rényi Maximum Correlation Coefficient. RDC is defined in terms of correlation of random non-linear copula projections; it is invariant with respect to marginal distribution transformations, has low computational cost and is easy to implement: just five lines of R code, included at the end of the paper."""
    
    print actual
    print expected
    assert_equals(actual, expected)
