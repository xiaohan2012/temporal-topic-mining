import numpy as np


def strengths_over_periods(period2matrix, topic_word_distribution,
                           n_top_words=15):
    """
    Calculate topic strengths over different periods

    Parameters:
    ------------
    period2matrix: dict<hashable -> (numpy.ndarray | scipy sparse matrix)>
        mapping from period to the document matrix of that period

    topic_word_distribution: numpyp.ndarray
        word distribution on each topic. Shape: (n_topics, vocab_size)
    
    n_top_words: int
        number of top words selected as the indicative for each topic
        only the topic words are counted towards the strength

    Returns:
    ------------
    dict<int -> numpy.ndarray>
        mapping from period to topic strengths during that period
        topic_strengths shape: (n_topics, )
    """
    top_word_ids_per_topic\
        = np.argsort(topic_word_distribution, axis=1)[:, -n_top_words:]

    period2strength = {}

    for period, X in period2matrix.items():
        topic_strengths = []

        for word_distribution, word_ids in zip(topic_word_distribution,
                                               top_word_ids_per_topic):
            strength = np.mean(  # normalize by corpuse size
                np.dot(X[:, word_ids].todense(),
                       word_distribution[word_ids])
            )
            
            topic_strengths.append(strength)
        period2strength[period] = np.asarray(topic_strengths)

    return period2strength
