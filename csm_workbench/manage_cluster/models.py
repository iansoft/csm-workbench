# _*_ coding: utf-8 _*_
from django.db import models

class Cluster(models.Model):
    '''
        the cluster
    '''
    name = models.CharField(max_length=45, null=True)
    host = models.CharField(max_length=45, null=True)
    class Meta:
        db_table = 't_cluster'
