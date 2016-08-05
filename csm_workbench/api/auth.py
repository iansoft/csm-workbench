# _*_ coding: utf-8 _*_
from django.db import connection
from manage_menu.models import Menu
from manage_account.models import Role, RoleMenu, Account
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

def get_role_list():
    '''
        get all the role
    '''
    dataset = Role.objects.filter(is_active=True)
    role_list = []
    for item in dataset:
        role = {
            "id":item.id,
            "name":item.name
        }
        role_list.append(role)
    return role_list


def get_domain_list():
    '''
        get the domain from keystone
    '''
    domain_list = [
        {"id":0, "name":"domain1"},
        {"id":1, "name":"domain2"}
    ]
    return domain_list


def create_account(account):
    '''
        account:{
            "username": "",
            "password": "",
            "role_id": "",
            "domain": "",
        }
           
        return
            0: success
            1: failed
    '''
    try:
        entity = Account(
                username = account["username"],
                password = account["password"],
                role_id = account["role_id"],
                domain = account["domain"]
            )
        entity.save()
        if entity.id != None:
            return 0
        else:
            return 1
    except Exception as e:
        print e