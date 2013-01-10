site:
	rm -rf output
	cp -r assets output
	python generate.py
local:
	rm -rf /usr/local/www/*
	cp -r output/* /usr/local/www
deploy:
	ssh -t longvie1@masenf.com masenf-com/deploy.sh
