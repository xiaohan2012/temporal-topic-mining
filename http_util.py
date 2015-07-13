import urllib2
from pyquery import PyQuery as pq


def download_jmlr_abstract(url):
    req = urllib2.urlopen(url)
    doc = pq(req.read())
    return doc.find("div#abstract").text()


def get_downloader_by_name(name):
    mapping = {"jmlr": download_jmlr_abstract}
    return mapping[name]
