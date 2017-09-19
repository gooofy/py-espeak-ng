all:	README.html

.PHONY:	tests clean

%.html: %.adoc
	asciidoctor -r asciidoctor-diagram -a toc $<

tests:
	nosetests

clean:
	rm -f *.html *.png

