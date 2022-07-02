.PHONY: docs site

docs:
	@mkdocs build

site:
	@python -m http.server --directory site --bind 127.0.0.1 80