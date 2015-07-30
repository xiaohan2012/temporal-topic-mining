import urllib2
from pyquery import PyQuery as pq


def download_jmlr_abstract(url):
    req = urllib2.urlopen(url)
    doc = pq(req.read())
    return doc.find("div#abstract").text()


def download_nips_abstract(url):
    return extract_content(url, "div.main p.abstract")


def extract_page_urls(page_url, link_parent_selector, link_selector):
    req = urllib2.urlopen(page_url)
    doc = pq(req.read())
    for a in doc(link_parent_selector):
        yield pq(a).find(link_selector).attr("href")


def extract_content(url, content_selector):
    req = urllib2.urlopen(url)
    doc = pq(req.read())
    return doc.find(content_selector).text()


def get_downloader_by_name(name):
    mapping = {"jmlr": download_jmlr_abstract,
               "nips": download_nips_abstract}
    return mapping[name]
