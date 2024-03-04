# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Server(models.Model):
    ip = models.GenericIPAddressField()
    status = models.CharField(max_length=50)
    user = models.CharField(max_length=100)
    key = models.TextField()
    port = models.PositiveIntegerField()
    operating_system = models.CharField(max_length=100)
    remarks = models.TextField()
