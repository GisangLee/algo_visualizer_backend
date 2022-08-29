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

        return np.random.choice(range(1, 100), max_size, replace=False)

    def __bubble_sort(self, data):

        loop = len(data) - 1

        sorted = False

        initial_data = copy.deepcopy(data)

        result = [initial_data]

        while not sorted:
            sorted = True

            for i in range(loop):

                if data[i] > data[i + 1]:

                    data[i], data[i + 1] = data[i + 1], data[i]

                    tmp = copy.deepcopy(data)
                    result.append(tmp)
                    sorted = False

            loop -= 1

        return result

    @swagger_auto_schema(manual_parameters=bubble_sorts_doc.bubble_sorts_list, tags = ["정렬 알고리즘"], operation_description="bubble, selection, insertionm merge, quick")
    def list(self, request, *args, **kwargs):

        sort_type = request.GET.get("sort_type", None)

        if sort_type is None:

            return Response(Error.error("정렬 타입을 지정해주세요."), status = status.HTTP_400_BAD_REQUEST)

        max_arr_size = int(request.GET.get("max_size", None))

        if max_arr_size is None:
            return Response(Error.error("데이터 크기를 정해주세요."), status = status.HTTP_400_BAD_REQUEST)


        if sort_type == "bubble":

            random_data = self.__make_random_array(max_size = max_arr_size)

            sorted_list = self.__bubble_sort(random_data)
            return Response(Success.response(self.__class__.__name__, request.method, sorted_list, "200"), status = status.HTTP_200_OK)
        else:
            return Response(Success.response(self.__class__.__name__, request.method, "만드는 중", "200"), status = status.HTTP_200_OK)



