import sys
import argparse
import urlparse

import codecs

from http_util import extract_page_urls


def main():
    parser = argparse.ArgumentParser(description="""Extract paper urls in the parent page.

Example:

python download_paper_urls.py \
--page_url "http://papers.nips.cc/book/advances-in-neural-information-processing-systems-26-2013" \
--link_parent_selector "div.main ul li" \
--link_selector "a:eq(0)" \
--output_path data/nips-2013.txt""")
    parser.add_argument("--page_url", required=True, type=str,
                        help="URL of the page that contains paper urls")
    parser.add_argument("--link_parent_selector", required=True, type=str,
                        help="CSS selector of the link parent element")
    parser.add_argument("--link_selector", required=True, type=str,
                        help="CSS selector of the link element")
    parser.add_argument("--output_path", required=True, type=str,
                        help="Path of file to save the result")
    
    args = parser.parse_args()
    urls = extract_page_urls(args.page_url, args.link_parent_selector,
                             args.link_selector)
    urls = list(urls)
    sys.stderr.write("Extracted {} urls from {}\n".format(
        len(urls), args.page_url))
    
    with codecs.open(args.output_path, "w", "utf8") as output_file:
        urls = map(lambda url: urlparse.urljoin(args.page_url, url),
                   urls)
        output_file.write("\n".join(urls))


if __name__ == "__main__":
    main()
