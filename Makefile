site:
	rm -rf output
	cp -r assets output
	/usr/local/bin/python generate.py
	rm -rf /usr/local/www/*
	cp -r output/* /usr/local/www
