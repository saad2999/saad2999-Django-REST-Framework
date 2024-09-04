from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_query_param='p'
    page_size_query_param='records'
    page_size = 5
    max_page_size = 10
    