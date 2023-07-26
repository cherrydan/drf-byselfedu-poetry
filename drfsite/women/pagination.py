from rest_framework.pagination import PageNumberPagination


class LeatherAPIListPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 100
