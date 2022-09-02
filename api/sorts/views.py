import copy
import json
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
from sorts.serializers import ser
from sorts import models as sort_models


class SortViewSet(mixins.BaseModelViewSet):
    # class SortViewSet(ModelViewSet):

    serializer_class = ser.TmpSer
    read_serializer_class = ser.TmpSer

    queryset = sort_models.Tmp.objects.all()

    def __make_random_array(self, max_size):

        return np.random.choice(range(1, 100), max_size, replace=False)

    def __generate_color_list(self, initial_data):

        colors = ["#424242" for i in range(len(initial_data))]
        return colors

    def __bubble_sort(self, data):

        loop = len(data) - 1

        sorted = False

        initial_data = copy.deepcopy(data)
        colors = self.__generate_color_list(initial_data)
        colors[0] = "#C74C4C"
        initial_color_data = copy.deepcopy(colors)

        result = [initial_data]
        color_result = [initial_color_data]

        # end = 2
        # reverse_idx = -1

        while not sorted:
            sorted = True

            for i in range(loop):

                if data[i] > data[i + 1]:

                    data[i], data[i + 1] = data[i + 1], data[i]

                    colors[i], colors[i + 1] = colors[i + 1], colors[i]

                    tmp = copy.deepcopy(data)
                    # color_tmp = copy.deepcopy(colors)

                    result.append(tmp)
                    # color_result.append(color_tmp)

                    sorted = False

            # last_color_set = color_result[-1]

            # print(f"last color set : {last_color_set}")
            # print(f"end : {end}")
            # print(f"reverse_idx : {reverse_idx}")

            # for _ in last_color_set[-1:-end:-1]:
            #     print(f"last color tmp : {last_color_set[reverse_idx]}")

            #     last_color_set[reverse_idx] = "#4BDEE1"

            # reverse_idx -= 1
            # end += 1

            # print(f"color_result : {color_result}")

            # end = idx + 1

            # print(f"colors : {color_result}")
            # print(f" data : {result}")

            loop -= 1

        response = {
            "data": result,
            "color": color_result
        }

        return response

    def __insertion_sort(self, data):

        result = []

        initial_data = copy.deepcopy(data)

        result.append(initial_data)

        for idx in range(1, len(data)):

            j = idx

            while j > 0 and data[j - 1] > data[j]:
                data[j - 1], data[j] = data[j], data[j - 1]
                tmp = copy.deepcopy(data)
                result.append(tmp)
                j -= 1

            # for idx in range(a, 0, -1):

            #     if data[idx] < data[idx - 1]:
            #         data[idx], data[idx - 1] = data[idx - 1], data[idx]
            #         tmp = copy.deepcopy(data)
            #         result.append(tmp)

            #     else:
            #         break

        response = {
            "data": result,
            "color": []
        }

        return response

    def __selection_sort(self, data):

        initial_data = copy.deepcopy(data)
        result = [initial_data]

        loop = len(data)

        for i in range(loop):

            min_idx = i
            for j in range(i+1, loop):

                if (data[min_idx] > data[j]):
                    min_idx = j

            data[i], data[min_idx] = data[min_idx], data[i]

            tmp = copy.deepcopy(data)
            result.append(tmp)

        response = {
            "data": result,
            "color": []
        }

        return response

    def __partition(self, list, start, end):
        pivot = list[start]
        left = start + 1
        right = end
        done = False

        while not done:

            while left <= right and list[left] <= pivot:
                left += 1

            while left <= right and list[right] > pivot:
                right -= 1

            if right < left:
                done = True

            else:
                list[left], list[right] = list[right], list[left]

        list[start], list[right] = list[right], list[start]  # 피봇 교환

        return [right, list]

    def __quick_sort(self, list, start, end):
        stack = []
        stack.append(start)
        stack.append(end)

        initial_data = copy.deepcopy(list)
        result = [initial_data]

        while stack:
            end = stack.pop()
            start = stack.pop()

            pivot, sorted_list = self.__partition(list, start, end)
            
            tmp = copy.deepcopy(sorted_list)
            result.append(tmp)

            if pivot - 1 > start:
                stack.append(start)
                stack.append(pivot - 1)

            if pivot + 1 < end:
                stack.append(pivot + 1)
                stack.append(end)

        response = {
            "data": result,
            "color": []
        }

        return response

    @swagger_auto_schema(manual_parameters=bubble_sorts_doc.bubble_sorts_list, tags=["정렬 알고리즘"], operation_description="bubble, selection, insertionm merge, quick")
    def list(self, request, *args, **kwargs):

        sort_type = request.GET.get("sort_type", None)

        if sort_type is None:

            return Response(Error.error("정렬 타입을 지정해주세요."), status=status.HTTP_400_BAD_REQUEST)

        data = request.GET.get("data", None)
        data = data.split(",")

        print(f"Data : {data}")

        data = [int(x) for x in data]

        if data is None:
            return Response(Error.error("정렬할 데이터가 필요합니다."), status=status.HTTP_400_BAD_REQUEST)

        if sort_type == "bubble":

            # random_data = self.__make_random_array(max_size=max_arr_size)s
            sorted_list = self.__bubble_sort(data)
            return Response(Success.response(self.__class__.__name__, request.method, sorted_list, "200"), status=status.HTTP_200_OK)

        elif sort_type == "insertion":

            sorted_list = self.__insertion_sort(data)
            return Response(Success.response(self.__class__.__name__, request.method, sorted_list, "200"), status=status.HTTP_200_OK)

        elif sort_type == "selection":
            sorted_list = self.__selection_sort(data)
            return Response(Success.response(self.__class__.__name__, request.method, sorted_list, "200"), status=status.HTTP_200_OK)

        elif sort_type == "quick":
            sorted_list = self.__quick_sort(data, 0, len(data) - 1)
            return Response(Success.response(self.__class__.__name__, request.method, sorted_list, "200"), status=status.HTTP_200_OK)

        else:
            return Response(Success.response(self.__class__.__name__, request.method, "만드는 중", "200"), status=status.HTTP_200_OK)
