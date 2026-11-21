from sqlalchemy import create_engine
from sqlalchemy.engine import URL



class Database:
    def __init__(self):
        self.provider = "mysql+pymysql"

        self.host = "appdata-1vpqsa.db.enzonic.com"
        self.port = 3306
        self.user = "u_nf0s6vqieq.appdata-1vpqsa"
        self.password = "yvHt2q2UnRFjmzRuiRYaF1uS78eQBwWF"
        self.database = "main"

        connection_url = URL.create(
            drivername=self.provider,
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
            query={"ssl-mode": "REQUIRED"}
        )

        self.engine = create_engine(
            connection_url,
            pool_pre_ping=True
        )

    def get_engine(self):
        return self.engine