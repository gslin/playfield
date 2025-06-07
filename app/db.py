from . import vault

import sqlalchemy

class DB():
    engine = None

    def getEngine(self):
        if self.engine is None:
            v = vault.Vault().getVault()

            d = v['DB_DATABASE']
            h = v['DB_HOST']
            p = v['DB_PASS']
            u = v['DB_USER']

            self.engine = sqlalchemy.create_engine(f"mysql+pymysql://{u}:{p}@{h}/{d}")

        return self.engine
