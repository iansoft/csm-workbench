# _*_ coding: utf-8 _*_
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "csm_workbench.settings")

application = get_wsgi_application()

from csm_config import role_config, menu_config, role_menu_config
from api.menu import init_menu
from api.auth import init_role, init_role_menu

if __name__ == '__main__':
    # init_menu(menu_config)
    # init_role(role_config)
    # init_role_menu(role_menu_config)