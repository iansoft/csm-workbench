# _*_ coding: utf-8 _*_
from django.db import models

class Menu(models.Model):
    '''menu item'''
    name = models.CharField(max_length=45, null=False)
    url = models.CharField(max_length=225, null=False)
    icon = models.CharField(max_length=45, null=True)
    openable = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    parentID =  models.IntegerField(null=True)
    deleted = models.BooleanField(default=True)

    class Meta:
        db_table = 't_menu'