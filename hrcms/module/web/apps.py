
from django.apps import AppConfig


class WebAppConfig(AppConfig):
    name = 'web'
    verbose_name = "Module WEB"

    def ready(self):

        """
        from feincms.module.page.models import Page

        pre_save.connect(page_check_options, sender=Page)
        post_save.connect(test, sender=Page)
        """
