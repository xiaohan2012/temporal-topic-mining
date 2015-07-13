from nose.tools import assert_equals
from http_util import download_jmlr_abstract


def test_download_jmlr_abstract():
    url = "http://jmlr.org/proceedings/papers/v32/samdani14.html"
    actual = download_jmlr_abstract(url)
    expected = """This paper presents a latent variable structured prediction model for discriminative supervised clustering of items called the Latent Left-linking Model (L3M). We present an online clustering algorithm for L3M based on a feature-based item similarity function. We provide a learning framework for estimating the similarity function and present a fast stochastic gradient-based learning technique. In our experiments on coreference resolution and document clustering, L3 M outperforms several existing online as well as batch supervised clustering techniques."""

    assert_equals(actual, expected)
