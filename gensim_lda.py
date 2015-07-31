import itertools
from gensim.models.ldamodel import LdaModel
from gensim.corpora import Dictionary

from mynlp.preprocess import (transform, ALL_PIPELINE_NAMES)
from util import load_line_corpus

import logging
logging.basicConfig(level=logging.INFO)


def proc_corpus(docs):
    """
    Preprocess the documents

    Param:
    ---------
    docs: list of string, 
          each string corresponds to a document
    
    Return:
    ---------
    docs: list of tokens(list of string), 
          each tokens corresponds to a preprocessed document
    """
    return [transform(doc, ALL_PIPELINE_NAMES)
            for doc in docs]


def main():
    collection_name = "nips"
    years = xrange(2010, 2015)  # 10 ~ 14
    n_topics = 10
    
    corpus_paths = map(lambda y: 
                       "data/{}-{}.dat".format(collection_name, y),
                       years)
    all_corpus = []
    year2corpus = {}
    for year, path in zip(years, corpus_paths):
        corpus = list(load_line_corpus(path))
        all_corpus.append(proc_corpus(corpus))
        year2corpus[year] = corpus

    all_corpus = list(itertools.chain.from_iterable(all_corpus))

    dictionary = Dictionary(all_corpus)
    all_corpus = [dictionary.doc2bow(doc)
                  for doc in all_corpus]

    import pdb
    pdb.set_trace()

    # print all_corpus
    model = LdaModel(all_corpus, num_topics=n_topics,
                     id2word=dictionary,
                     eval_every=10, passes=100)
    print model.show_topics()


if __name__ == "__main__":
    main()
