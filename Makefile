.PHONY: serve build pdf

serve:
	mdbook serve

build:
	mdbook build

pdf: build
	@echo "PDF generated at book/pdf/output.pdf"
