#
.DEFAULT_GOAL:=	test
.PHONY:		deploy syntax test

#
# Targets
deploy:: syntax
	rsync -Favz --delete-after ./ ${SSH_USER}@${SSH_HOST}:playfield/
	ssh ${SSH_USER}@${SSH_HOST} 'cd playfield && scripts/deploy.sh'

syntax::
	uv run --python pypy3 python -m py_compile app.py

test:: syntax
	@true

-include GNUmakefile.local
