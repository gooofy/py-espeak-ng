all:	README.html README

.PHONY:	tests clean dist

%.html: %.adoc
	asciidoctor -r asciidoctor-diagram -a toc $<


README:	README.adoc
		cp README.adoc README

tests:
	nosetests

dist:
	python setup.py sdist

clean:
	rm -f *.html *.png README 
	rm -rf dist espeakng.egg-info

