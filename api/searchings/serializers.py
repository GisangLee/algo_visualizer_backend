from rest_framework import serializers
from searchings import models as searching_models

class SearchSer(serializers.ModelSerializer):

    class Meta:
        model = searching_models.STmp
        fields = ("pk", "s_name",)