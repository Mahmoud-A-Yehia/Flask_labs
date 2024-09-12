class Config:
    @staticmethod
    def init_app():
        pass

class DevelopmentConfig(Config):
    # static attributes
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db" # postgresql

    # SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"

class ProductionConfig(Config):
    DEBUG = True
    # mysql://username:password@server:port/db
    # postgresql://username:password@server:port/db
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db" # postgresql


config_options = {
    "dev":DevelopmentConfig,
    'prd':ProductionConfig
}