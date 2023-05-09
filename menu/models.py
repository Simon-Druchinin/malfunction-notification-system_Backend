from django.db import models


class NavigationMenu(models.Model):
    title = models.CharField(max_length=127)
    icon = models.CharField(max_length=63, default='', blank=True, null=True)
    navLink = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)

class DropDownMenu(models.Model):
    title = models.CharField(max_length=63, default='', blank=True, null=True)
    type = models.CharField(max_length=63, default='', blank=True, null=True)
    icon = models.CharField(max_length=63, default='', blank=True, null=True)
    navLink = models.CharField(max_length=255, blank=True, null=True)
