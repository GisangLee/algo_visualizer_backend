from audioop import minmax
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from searchings import serializers
from searchings import models as searching_models
from utils import mixins
from utils.success import Success
from utils.errors import Error


class SearchViewSet(mixins.BaseModelViewSet):

    serializer_class = serializers.SearchSer
    read_serializer_class = serializers.SearchSer

    queryset = searching_models.STmp.objects.all()

    def list(self, request):

        return Response(Success.response(self.__class__.__name__, request.method, "테스트", 200), status=status.HTTP_200_OK)
