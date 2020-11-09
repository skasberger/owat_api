import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Setting the default environment settings.
    """

    DEBUG = os.environ.get("DEBUG") or False
    API_PREFIX = "/api"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "my-secret-key"
    ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL") or None
    APP_EMAIL = os.environ.get("APP_EMAIL") or None
    TRAVIS = False
    MIN_CONNECTIONS_COUNT = os.environ.get("MIN_CONNECTIONS_COUNT") or None
    MAX_CONNECTIONS_COUNT = os.environ.get("MAX_CONNECTIONS_COUNT") or None
    TITLE = os.environ.get("TITLE") or "owat_api"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """
    Setting the development environment settings.
    Database is sqlite file or a postgresql database string passed by an environment variable.
    """

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DEV_DATABASE_URI") or "postgresql://localhost/owat_dev"
    )

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("TEST_DATABASE_URI") or "postgresql://localhost/owat_test"
    )

    ADMIN_EMAIL = "testing@offenewahlen.at"
    APP_EMAIL = "testing@offenewahlen.at"


class TravisConfig(TestingConfig):
    """
    Setting the test environment settings.
    """

    TRAVIS = True
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://postgres@localhost:5432/travis_ci_test"
    )


class ProductionConfig(Config):
    """
    Setting the production environment settings.
    """

    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("PROD_DATABASE_URI") or "postgresql://localhost/owat"
    )

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
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DOCKER_DATABASE_URI") or "postgresql://localhost/owat"
    )

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
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DOCKER_COMPOSE_DATABASE_URI")
        or "postgresql://postgres:postgres@localhost/owat"
    )

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
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "travis": TravisConfig,
    "docker": DockerConfig,
    "docker_compose": DockerComposeConfig,
    "unix": UnixConfig,
    "default": DevelopmentConfig,
}
