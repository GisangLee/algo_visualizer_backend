import copy
import numpy as np
from django.shortcuts import render
from rest_framework import permissions, filters, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from utils import mixins
from utils.errors import Error
from utils.success import Success
from utils.swaggers import bubble_sorts_doc

class SortViewSet(mixins.BaseModelViewSet):

    def __make_random_array(self, max_size):

        return np.random.choice(range(1, max_size + 10), max_size, replace=False)

    def __bubble_sort(self, data):

        loop = len(data) - 1

        sorted = False

        result = []

        while not sorted:
            sorted = True

            for i in range(loop):
                tmp = copy.deepcopy(data)

                if data[i] > data[i + 1]:

                    data[i], data[i + 1] = data[i + 1], data[i]
                    result.append(tmp)
                    sorted = False

            loop -= 1

        return result

    @swagger_auto_schema(manual_parameters=bubble_sorts_doc.bubble_sorts_list, tags = ["선형 검색"], operation_description="선형검색")
    def list(self, request, *args, **kwargs):

        sort_type = request.GET.get("sort_type", "linear")
        max_arr_size = int(request.GET.get("max_size", 50))

        random_data = self.__make_random_array(max_size = max_arr_size)

        sorted_list = self.__bubble_sort(random_data)
        return Response(Success.response(self.__class__.__name__, request.method, sorted_list, "200"), status = status.HTTP_200_OK)



