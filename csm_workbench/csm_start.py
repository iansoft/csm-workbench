# _*_ coding: utf-8 _*_
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "csm_workbench.settings")

from csm_config import role_config, menu_config, role_menu_config
from api.menu import init_menu
from api.auth import init_role, init_role_menu

if __name__ == '__main__':
    # build the menu tree
    #init_menu(menu_config)
    init_role(role_config)
    init_role_menu(role_menu_config)