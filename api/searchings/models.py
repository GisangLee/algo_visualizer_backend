from django.db import models

# Create your models here.

class STmp(models.Model):

    s_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "s_tmp"