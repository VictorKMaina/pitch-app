import os


class Config:
    """
    General configuration class
    """
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    """
    Class for Production configurations. Child of Config class.
    """
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    """
    Class for Test configurations. Child of Config class.
    """
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://victormainak:password@localhost/pitch_test"

class DevConfig(Config):
    """
    Class for Development configurations. Child of Config class.
    """
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://victormainak:password@localhost/pitch"
    DEBUG = True

config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}