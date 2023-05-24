# targets that aren't filenames
.PHONY: all clean deploy build serve run

all: build

BIBBLE = bibble

_includes/pubs.html: bib/pubs.bib bib/publications.tmpl
	mkdir -p _includes
	$(BIBBLE) $+ > $@

build: _includes/pubs.html
	jekyll build --destination /var/www/qkdlab_website

# you can configure these at the shell, e.g.:
# SERVE_PORT=5001 make serve
SERVE_HOST ?= server.gaokeyan.xyz
SERVE_PORT ?= 5000

serve: _includes/pubs.html
	jekyll serve --trace --port $(SERVE_PORT) --host $(SERVE_HOST)

clean:
	$(RM) -r _site _includes/pubs.html

DEPLOY_HOST ?= qkdlab.gaokeyan.xyz
DEPLOY_PATH ?= /var/www/qkdlab.gaokeyan.xyz/
RSYNC := rsync --compress --recursive --checksum --itemize-changes --delete -e ssh

deploy: clean build
	$(RSYNC) ../qkdlab_website/ ubuntu@qkdlab.gaokeyan.xyz:/home/ubuntu/qkdlab_website
