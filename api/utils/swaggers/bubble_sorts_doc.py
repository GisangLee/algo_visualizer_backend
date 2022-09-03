import os
from drf_yasg import openapi


def make_api_param(name, type, desc, format, default=""):
    param = openapi.Parameter(
        name,
        type,
        description=desc,
        type=format,
        default=default
    )

    return param

base_api_param = [
    make_api_param("data", openapi.IN_QUERY, "데이터 ( 배열 ) ", openapi.TYPE_STRING),
    make_api_param("sort_type", openapi.IN_QUERY, "정렬 타입 ( bubble, selection, insertion, merge, quick 중 택 1 )", openapi.TYPE_STRING),
]

search_base_api_param = [
    make_api_param("data", openapi.IN_QUERY, "데이터 ( 배열 ) ", openapi.TYPE_STRING),
    make_api_param("target", openapi.IN_QUERY, "타겟 데이터 ( 정수 ) ", openapi.TYPE_STRING),
    make_api_param("search-type", openapi.IN_QUERY, "정렬 타입 ( linear, binary 중 택 1 )", openapi.TYPE_STRING),
]

auth_api_param = [
    make_api_param("system_key", openapi.IN_HEADER, "시스템 key", openapi.FORMAT_INT64, default=f"key {os.environ.get('SECRET_KEY')}"),
]

bubble_sorts_list = base_api_param + auth_api_param

search_algo = search_base_api_param + auth_api_param