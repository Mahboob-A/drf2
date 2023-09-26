

from rest_framework.pagination import LimitOffsetPagination 


class DemoPagination(LimitOffsetPagination): 
        page_size = 3 
        default_limit = 3
        max_limit = 8 
        # limit_query_param = 'lim'
        # offset_query_param = 'offs'
        