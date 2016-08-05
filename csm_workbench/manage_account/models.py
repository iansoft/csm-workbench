# _*_ coding: utf-8 _*_
from django.db import models
from manage_menu.models import Menu

class Role(models.Model):
    '''
        The roles for csm 
        Sync with keystone roles
    '''
    name = models.CharField(max_length=45, null=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        db_table = 't_role'

class RoleMenu(models.Model):
    '''
        bind the role with menus
    '''
    role = models.ForeignKey(Role)
    menu = models.ForeignKey(Menu)
    class Meta:
        db_table = 't_role_menu'


class Account(models.Model):
    '''
        The account for csm 
    '''
    role = models.ForeignKey(Role, null=True)
    username = models.CharField(max_length=45, null=True)
    password = models.CharField(max_length=45, null=True)
    domain = models.CharField(max_length=45, null=True)
    class Meta:
        db_table = 't_account'