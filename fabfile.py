from armstrong.dev.tasks import *
from fabric.api import task


settings = {
    'DEBUG': True,
    'INSTALLED_APPS': (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'armstrong.core.tt_sections',
        'armstrong.core.tt_sections.tests.tt_sections_support',
        'lettuce.django',
        'south',
        'mptt',
    ),
    'ROOT_URLCONF': 'armstrong.core.tt_sections.tests.tt_sections_support.urls',
    'SITE_ID': 1,
    'ARMSTRONG_SECTION_ITEM_MODEL': 'armstrong.core.tt_sections.tests.tt_sections_support.models.SimpleCommon',
}

full_name = "armstrong.core.tt_sections"
main_app = "tt_sections"
tested_apps = (main_app, )
pip_install_first = True
