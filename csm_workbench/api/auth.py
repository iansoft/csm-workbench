# _*_ coding: utf-8 _*_
from django.db import connection
from manage_menu.models import Menu
from manage_account.models import Role, RoleMenu
from sqlhelper import dictfetchall

def init_role(role_config):
    for name in role_config:
        role = Role(name=name)
        role.save()

def init_role_menu(role_menu_config):
    for item in role_menu_config:
        role = Role.objects.get(name=item["role"])
        for m in item["menu_list"]:
            try:
                menu = Menu.objects.get(name=m)
                group_menu = RoleMenu(role=role, menu=menu)
                group_menu.save()
            except ObjectDoesNotExist:
                print("Menu doesn't exist. %s"%(m))

