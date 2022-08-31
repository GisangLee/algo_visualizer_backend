from rest_framework import serializers
from sorts import models as sort_models

class TmpSer(serializers.ModelSerializer):


    class Meta:
        model = sort_models.Tmp
        fields = ("pk", "name",)