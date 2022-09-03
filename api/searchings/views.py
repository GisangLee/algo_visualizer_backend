import copy
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from searchings import serializers
from searchings import models as searching_models
from utils import mixins
from utils.swaggers import bubble_sorts_doc
from utils.success import Success
from utils.errors import Error


class SearchViewSet(mixins.BaseModelViewSet):

    serializer_class = serializers.SearchSer
    read_serializer_class = serializers.SearchSer

    queryset = searching_models.STmp.objects.all()

    def __linear_search(self, data, targaet):
        """ 선형탐색

        Args:
            data ( list ): 선형탐색 초기 데이터

        Returns:
            result ( list ): 선형탐색 과정이 전부 담긴 2차원 배열 

        """
        result = []

        for i in range(len(data)):
            result.append(i)

            if targaet == data[i]:
                break

        return result

    def __binary_search(self, data, target):
        """ 이진 탐색 

        Args:
            data (list): 이진탐색 초기 데이터

        Returns
            result (list): 이진탐색 과정이 전부 담긴 2차원 배열

        """

        result = {
            "start":[],
            "end": [],
            "mid": []
        }

        # data.sort()

        print(f"data : {data}")

        start = 0
        end = len(data) - 1

        while start <= end:
            mid = (start + end) // 2

            print(f"mid : {mid}")

            print(f"data[mid] : {data[mid]}")
            print(f"target : {target}")

            if data[mid] == target:
                result["mid"].append(mid)
                result["start"].append(start)
                result["end"].append(end)

                break

            elif data[mid] < target:
                start = mid + 1
                print(f"start : {start}")



            else:
                end = mid - 1

            result["mid"].append(mid)
            result["start"].append(start)
            result["end"].append(end)

        return result

    def __hash_search(self, data):
        """ 해시 탐색

        Args:
            data (list): 해시탐색 초기 데이터

        Returns:
            result (list): 해시 탐색 과정이 전부 담긴 2차원 배열 

        """

        return 0

    @swagger_auto_schema(manual_parameters=bubble_sorts_doc.search_algo, tags=["탐색 알고리즘"], operation_description="linear, binary")
    def list(self, request):

        search_type = request.GET.get("search_type", None)
        initial_data = request.GET.get("data", None)
        target = request.GET.get("target", None)

        if search_type is None or initial_data is None or target is None:
            return Response(Error.error("데이터 혹은 탐색 알고리즘 모두 지정 해야합니다."), status=status.HTTP_400_BAD_REQUEST)

        data = initial_data.split(",")
        data = [int(x) for x in data]

        target = int(target)

        if search_type == "linear":
            searched_index = self.__linear_search(data, target)
            return Response(Success.response(self.__class__.__name__, request.method, searched_index, 200))

        elif search_type == "binary":
            searched_index = self.__binary_search(data, target)
            return Response(Success.response(self.__class__.__name__, request.method, searched_index, 200))

        elif search_type == "hash":
            searched_index = self.__hash_search(data, target)
            return Response(Success.response(self.__class__.__name__, request.method, searched_index, 200))

        else:
            return Response(Error.error("올바른 탐색 알고리즘이 아닙니다."), status=status.HTTP_400_BAD_REQUEST)
