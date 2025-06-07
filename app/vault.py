import json

vault_json = '/srv/vault/playfield/default.current.json'
vault = {}

with open(vault_json, 'r') as f:
    vault = json.load(f)
