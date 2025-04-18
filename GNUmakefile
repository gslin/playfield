#
.DEFAULT_GOAL:=	test
.PHONY:		deploy test

#
# Targets
deploy::
	rsync -Favz --delete-after ./ ${SSH_USER}@${SSH_HOST}:playfield/

test::
	@true

-include GNUmakefile.local
