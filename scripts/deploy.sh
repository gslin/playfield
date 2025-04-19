#!/bin/sh

set -eou pipefail

mkdir -p ~/.config/systemd/user || true
cp playfield.service ~/.config/systemd/user/playfield.service
systemctl --user daemon-reload
systemctl --user enable playfield
systemctl --user restart playfield
