site:
	rm -rf output
	cp -r assets output
	python generate.py
test:
	rm -rf /home/masen/public_html/stage
	cp -R output/ /home/masen/public_html/stage
