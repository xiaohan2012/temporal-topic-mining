import sys
import argparse
import codecs
from http_util import get_downloader_by_name

def main():
    parser = argparse.ArgumentParser(description="Paper abstract downloader cmd tool")
    parser.add_argument("--site", required=True, type=str,
                        help="The name of site that hosts the papers. JMLR for example")
    parser.add_argument("--urlpath", required=True, type=str,
                        help="The file that stores the urls of the paper")
    parser.add_argument("--output_path", required=True, type=str,
                        help="Path of file to save the result")
    
    args = parser.parse_args()
    try:
        download = get_downloader_by_name(args.site)
    except KeyError:
        print "Unable to download '{}' for now".format(args.site)
        sys.exit(-1)

    
    with open(args.urlpath, "r") as f, \
         codecs.open(args.output_path, "w", "utf8") as output_file:
        for i, l in enumerate(f):
            if i % 20 == 0:
                print "Downloaded {} abstracts".format(i)
            content = download(l.strip())
            output_file.write(u"{}\n".format(content))
            i += 1


if __name__ == "__main__":
    main()
