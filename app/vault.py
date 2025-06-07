import json

_vault = None

class Vault:
    vault_json = '/srv/vault/playfield/default.current.json'

    def __init__(self):
        global _vault
        if _vault:
            return
        with open(self.vault_json, 'r') as f:
            _vault = json.load(f)

    def getVault(self):
        global _vault
        return _vault
