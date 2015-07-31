import lda
import itertools
import numpy as np
import codecs
from temporal import strengths_over_periods

from sklearn.feature_extraction.text import CountVectorizer

from mynlp.preprocess import (transform, ALL_PIPELINE_NAMES)
from util import load_line_corpus


def main():
    # parameters
    collection_name = "nips"
    years = xrange(2008, 2015)  # 10 ~ 14
    n_topics = 10
    n_top_words = 15
    
    # load corpus
    corpus_paths = map(lambda y: 
                       "data/{}-{}.dat".format(collection_name, y),
                       years)
    all_corpus = []
    year2corpus = {}
    for year, path in zip(years, corpus_paths):
        corpus = list(load_line_corpus(path))
        all_corpus.append(corpus)
        year2corpus[year] = corpus

    all_corpus = list(itertools.chain.from_iterable(all_corpus))

    preprocessor = lambda doc: ' '.join(transform(doc, ALL_PIPELINE_NAMES))
    tokenizer = lambda doc: doc.split()
    
    with codecs.open('data/lemur-stopwords.txt', 
                     'r' 'utf8') as f:
        stop_words = map(lambda s: s.strip(), f.readlines())

    vectorizer = CountVectorizer(preprocessor=preprocessor,
                                 tokenizer=tokenizer,
                                 stop_words=stop_words,
                                 min_df=5)

    X = vectorizer.fit_transform(all_corpus)

    id2word = {id_: word
               for word, id_ in vectorizer.vocabulary_.items()}
    
    # build the model
    model = lda.LDA(n_topics=n_topics, n_iter=500,
                    # alpha=1.0, eta=1.0,
                    random_state=1)
    model.fit(X)
    
    # print topics
    for i, topic_dist in enumerate(model.topic_word_):
        top_word_ids = np.argsort(topic_dist)[:-n_top_words:-1]
        topic_words = [id2word[id_] for id_ in top_word_ids]
        print('Topic {}: {}'.format(i, ' '.join(topic_words)))
        
    year2matrix = {}
    start_document_index = 0

    for year in years:
        corpus_size = len(year2corpus[year])
        end_document_index = start_document_index + corpus_size
        year2matrix[year] = X[start_document_index: end_document_index, :]
        start_document_index = end_document_index

    tbl = strengths_over_periods(year2matrix, model.topic_word_,
                                 n_top_words=50)
    print np.array(tbl.values())

if __name__ == "__main__":
    main()
