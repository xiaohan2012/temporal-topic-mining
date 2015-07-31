#! /bin/bash

years=(2008 2009)

for year in ${years[@]}; do
	echo "Downloading urls of ${year}..."
	python download_paper_urls.py \
		--page_url "http://papers.nips.cc/book/year-${year}" \
		--link_parent_selector "div.main ul li" \
		--link_selector "a:eq(0)" \
		--output_path data/nips-${year}.txt

	echo "Downloading papers of ${year}..."
	python download_abstract.py --site nips \
		--urlpath data/nips-${year}.txt \
		--output_path data/nips-${year}.dat
done



