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
            "start": [],
            "end": [],
            "mid": []
        }

        start = 0
        end = len(data) - 1

        while start <= end:
            mid = (start + end) // 2

            result["mid"].append(mid)
            result["start"].append(start)
            result["end"].append(end)

            if data[mid] == target:
                result["mid"].append(mid)
                result["start"].append(mid)
                result["end"].append(mid)

                break

            elif data[mid] < target:
                start = mid + 1

            else:
                end = mid - 1

        return result

    def __hash_table(self, data):

        list_by_zeros = [0 for i in round(len(data) * 1.5 + 0.5)]

        for i in range(len(data)):
            key = data[i] % 11

            if (list_by_zeros[key] == None):
                list_by_zeros[key] = data[i]
            else:
                while (list_by_zeros[key]):
                    if (key < len(list_by_zeros)-1):
                        key += 1
                    else:
                        key = 0

                list_by_zeros[key] = data[i]

        return list_by_zeros

    def __hash_search(self, data, target):
        """ 해시 탐색

        Args:
            data (list): 해시탐색 초기 데이터

        Returns:
            result (list): 해시 탐색 과정이 전부 담긴 2차원 배열

        """
        k = target % len(data)

        while data[k] is not 0:

            if data[k] is target:
                return k

            else:
                k = (k+1) % len(data)

        return 'Not Found'

    @ swagger_auto_schema(manual_parameters=bubble_sorts_doc.search_algo, tags=["탐색 알고리즘"], operation_description="linear, binary")
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

            hash_table = self.__hash_table(data)
            print(f"hash table : {hash_table}")
            # searched_index = self.__hash_search(hash_table, target)
            # print(f"result : {searched_index}")
            return Response(Success.response(self.__class__.__name__, request.method, searched_index, 200))

        else:
            return Response(Error.error("올바른 탐색 알고리즘이 아닙니다."), status=status.HTTP_400_BAD_REQUEST)
