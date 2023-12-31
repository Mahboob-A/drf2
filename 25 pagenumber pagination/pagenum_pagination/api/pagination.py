

from rest_framework.pagination import PageNumberPagination


class DemoPagination(PageNumberPagination): 
        page_size = 3 
        page_query_param = 'p'
        page_size_query_param = 'size'
        max_page_size = 10 
        last_page_strings = ['last', 'end']