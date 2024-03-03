# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Events(models.Model):

    #__Events_FIELDS__
    event_name = models.CharField(max_length=255, null=True, blank=True)
    event_description = models.CharField(max_length=255, null=True, blank=True)

    #__Events_FIELDS__END

    class Meta:
        verbose_name        = _("Events")
        verbose_name_plural = _("Events")


class User(models.Model):

    #__User_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Costs(models.Model):

    #__Costs_FIELDS__
    what = models.CharField(max_length=255, null=True, blank=True)
    howmuch = models.CharField(max_length=255, null=True, blank=True)

    #__Costs_FIELDS__END

    class Meta:
        verbose_name        = _("Costs")
        verbose_name_plural = _("Costs")



#__MODELS__END
