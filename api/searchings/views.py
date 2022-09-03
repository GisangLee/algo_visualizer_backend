import copy
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

    def __binary_search(self, data):
        """ 이진 탐색 

        Args:
            data (list): 이진탐색 초기 데이터

        Returns
            result (list): 이진탐색 과정이 전부 담긴 2차원 배열

        """
        return 0

    def __hash_search(self, data):
        """ 해시 탐색

        Args:
            data (list): 해시탐색 초기 데이터

        Returns:
            result (list): 해시 탐색 과정이 전부 담긴 2차원 배열 

        """

        return 0

    def list(self, request):

        search_type = request.GET.get("search_type", None)

        initial_data = request.GET.get("data", None)

        target = request.GET.get("target", None)

        print(f"search type : {search_type}")
        print(f"initial_data : {initial_data}")
        print(f"target : {target}")
        
        data = initial_data.split(",")

        print(f"Data : {data}")

        data = [int(x) for x in data]

        print(f"data convert to int : {data}")


        if search_type is None or initial_data is None or target is None:

            return Response(Error.error("데이터 혹은 탐색 알고리즘 모두 지정 해야합니다."), status=status.HTTP_400_BAD_REQUEST)

        if search_type == "linear":
            searched_index = self.__linear_search(initial_data, target)
            return Response(Success.response(self.__class__.__name__, request.method, searched_index, 200))

        elif search_type == "binary":
            searched_index = self.__binary_search(initial_data, target)
            return Response(Success.response(self.__class__.__name__, request.method, searched_index, 200))

        elif search_type == "hash":
            searched_index = self.__hash_search(initial_data, target)
            return Response(Success.response(self.__class__.__name__, request.method, searched_index, 200))

        else:
            return Response(Error.error("올바른 탐색 알고리즘이 아닙니다."), status=status.HTTP_400_BAD_REQUEST)
