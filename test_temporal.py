import numpy as np

from scipy.sparse import csr_matrix

from nose.tools import assert_equal

from temporal import strengths_over_periods


def test_strengths_over_periods():
    # words: topic, mining, computer, vision
    # 2 docs, 4 words
    period2matrix = {'p1': csr_matrix(np.asarray([[1, 1, 0, 0],
                                                  [2, 1, 1, 0]])),
                     'p2': csr_matrix(np.asarray([[1, 0, 1, 2],
                                                  [0, 0, 2, 1]]))}
    
    # 2 topics, 4 words
    topic_word_distribution = np.asarray([[0.6, 0.4, 0.000001, 0.000001],
                                          [0.000001, 0.000001, 0.5, 0.5]])
    
    period2strengh = strengths_over_periods(period2matrix,
                                            topic_word_distribution,
                                            n_top_words=2)
    
    assert_equal(len(period2strengh), 2)
    
    for p in ['p1', 'p2']:
        assert_equal(period2strengh[p].shape, (2, ))

    assert_equal(period2strengh['p1'][0], 1.3)  # (0.6 + 0.4 + 1.2 + 0.4) / 2
    assert_equal(period2strengh['p1'][1], 0.25)  # (0.5 + 0) / 2

    assert_equal(period2strengh['p2'][0], 0.3)  # (0.6 + 0) / 2
    assert_equal(period2strengh['p2'][1], 1.5)  # (0.5 + 1.5 + 1.5 + 0.5) / 2

