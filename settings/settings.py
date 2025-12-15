from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/
# SECURITY WARNING
SECRET_KEY = "django-insecure-97amey_4u*noy-$$3&72-3il%@v0puf7iee75%nb98dmd@=$#$"
DEBUG = True
ALLOWED_HOSTS = []


# Application Definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "settings.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "settings.wsgi.application"


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password Validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static Files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/
STATIC_URL = "static/"


# Task Back-end
TASKS = {
    "servicebus_queue": {
        "BACKEND": "cloud_tasks_azure.backends.service_bus.ServiceBusQueueBackend",
        "QUEUES": ["email-ingestor"],
        "OPTIONS": {
            "SERVICEBUS_DEFAULT_QUEUE_NAME": "testing",
            "SERVICEBUS_USE_CONNECTION_STRING": True,
            "SERVICEBUS_CONNECTION_STRING": "",
            "SERVICEBUS_NAMESPACE_FQDN": "",
        },
    },
    "servicebus_topic": {
        "BACKEND": "cloud_tasks_azure.backends.service_bus.ServiceBusTopicBackend",
        "QUEUES": ["email-ingestor-topic"],
        "OPTIONS": {
            "SERVICEBUS_DEFAULT_TOPIC_NAME": "testing",
            "SERVICEBUS_USE_CONNECTION_STRING": True,
            "SERVICEBUS_CONNECTION_STRING": "",
            "SERVICEBUS_NAMESPACE_FQDN": "",
            "SERVICEBUS_CREDENTIAL_LOADER": "this.that.custom_credential_loader_function",
        },
    },
    "sa_queue": {
        "BACKEND": "cloud_tasks_azure.backends.sa_queue.StorageAccountQueueBackend",
        "QUEUES": ["email-ingestor"],
        "OPTIONS": {
            "STORAGE_ACCOUNT_QUEUE_DEFAULT_QUEUE_NAME": "testing",
            "STORAGE_ACCOUNT_USE_CONNECTION_STRING": True,
            "STORAGE_ACCOUNT_CONNECTION_STRING": "",
            "STORAGE_ACCOUNT_URL": "",
            "STORAGE_ACCOUNT_CREDENTIAL_LOADER": "this.that.custom_credential_loader_function",
        },
    },
    "sqs": {
        "BACKEND": "cloud_tasks_aws.backends.SQSBackend",
        "QUEUES": ["email-ingestor"],
        "OPTIONS": {
            "AWS_DEFAULT_QUEUE_NAME": "testing",
            "AWS_REGION": "ap-south-1",
        },
    },
    "sns": {
        "BACKEND": "cloud_tasks_aws.backends.SNSTopicBackend",
        "QUEUES": ["email-ingestor"],
        "OPTIONS": {
            "AWS_DEFAULT_TOPIC_NAME": "testing",
            "AWS_SNS_ARN_PREFIX": "arn:aws:sns:<region>:<account-number>:",
            "AWS_REGION": "ap-south-1",
        },
    },
    "eventbridge_scheduler": {
        "BACKEND": "cloud_tasks_aws.backends.EventBridgeSchedulerBackend",
        "QUEUES": ["email-ingestor"],
        "OPTIONS": {
            "AWS_DEFAULT_SQS_QUEUE_NAME": "testing",
            "EVENTBRIDGE_SCHEDULER_ROLE_ARN": "",
            "AWS_REGION": "ap-south-1",
        },
    },
}
