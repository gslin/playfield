#!/bin/sh

set -eou pipefail

# pypy
rm -fr .venv
mise exec uv@latest -- uv venv --python pypy3

# systemd
mkdir -p ~/.config/systemd/user || true
cp playfield.service ~/.config/systemd/user/playfield.service
systemctl --user daemon-reload
systemctl --user enable playfield
systemctl --user restart playfield
