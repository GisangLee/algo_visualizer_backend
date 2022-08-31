from django.db import models



class Tmp(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "tmp"