from enum import Enum


class SeverityLevel(str, Enum):

    INFO = "INFO"

    WARNING = "WARNING"

    ERROR = "ERROR"

    CRITICAL = "CRITICAL"


class Environment(str, Enum):

    DEVELOPMENT = "development"

    STAGING = "staging"

    PRODUCTION = "production"


class EventSource(str, Enum):

    PROMETHEUS = "prometheus"

    LOKI = "loki"

    JAEGER = "jaeger"

    KUBERNETES = "kubernetes"

    DEPLOYMENT = "deployment"