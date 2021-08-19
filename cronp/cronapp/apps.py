from django.apps import AppConfig


class CronappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cronapp'

    def ready(self):
        from .views import start
        start()
