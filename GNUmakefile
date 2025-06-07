#
.DEFAULT_GOAL:=	test
.PHONY:		clean deploy lint syntax test

#
# Targets
clean::
	rm -rf .venv

deploy:: syntax lint
	rsync -Favz --delete-after ./ ${SSH_USER}@${SSH_HOST}:playfield/
	ssh ${SSH_USER}@${SSH_HOST} 'cd playfield && scripts/deploy.sh'

lint::
	uv run --python pypy3 ruff check app/

syntax::
	uv run --python pypy3 python -m py_compile app/*.py

test:: syntax lint
	@true

-include GNUmakefile.local
