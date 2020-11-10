import os
from pydantic import BaseSettings, PostgresDsn
from functools import lru_cache


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(BaseSettings):
    DEBUG: bool = False
    API_PREFIX: str = "/api"
    SECRET_KEY: str = "my-secret-key"
    ADMIN_EMAIL: str = None
    APP_EMAIL: str = None
    TRAVIS: bool = False
    MIN_CONNECTIONS_COUNT: int = None
    MAX_CONNECTIONS_COUNT: int = None
    TITLE: str = "owat_api"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI: str = "postgresql://localhost/owat_dev"

    DEBUG: bool = True

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI: str = "postgresql://localhost/owat_test"

    DEBUG: bool = False

    class Config:
        env_file = ".env.testing"

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class TravisConfig(Config):
    SQLALCHEMY_DATABASE_URI: str = "postgresql+psycopg2://postgres@localhost:5432/travis_ci_test"

    DEBUG: bool = False
    TRAVIS = True

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI: str = "postgresql://localhost/owat"

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        import logging
        from logging.handlers import RotatingFileHandler

        if not os.path.exists("logs"):
            os.mkdir("logs")

        file_handler = RotatingFileHandler(
            "logs/owatapi.log", maxBytes=10240, backupCount=10
        )

        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
            )
        )
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info("Offene Wahlen AT API")


class DockerConfig(ProductionConfig):
    SQLALCHEMY_DATABASE_URI: str = "postgresql://localhost/owat_docker"

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler

        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


class DockerComposeConfig(DockerConfig):
    SQLALCHEMY_DATABASE_URI: str = "postgresql://localhost/owat_dockercompose"

    @classmethod
    def init_app(cls, app):
        DockerConfig.init_app(app)


class UnixConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to syslog
        import logging
        from logging.handlers import SysLogHandler

        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.INFO)
        app.logger.addHandler(syslog_handler)


def get_config_name():
    return os.getenv("FASTAPI_CONFIG") or "default"


config = {
    "development": DevelopmentConfig(),
    "testing": TestingConfig(),
    "production": ProductionConfig(),
    "travis": TravisConfig(),
    "docker": DockerConfig(),
    "docker_compose": DockerComposeConfig(),
    "unix": UnixConfig(),
    "default": DevelopmentConfig(),
}
