#
.DEFAULT_GOAL:=	test
.PHONY:		deploy test

#
# Targets
deploy::
	rsync -Favz --delete-after ./ ${SSH_USER}@${SSH_HOST}:playfield/
	ssh ${SSH_USER}@${SSH_HOST} 'cd playfield && scripts/deploy.sh'

test::
	uv run --python pypy3 python -m py_compile app.py

-include GNUmakefile.local
