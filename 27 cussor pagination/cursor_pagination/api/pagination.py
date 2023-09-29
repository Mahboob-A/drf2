

from rest_framework.pagination import CursorPagination


class CustomCursorPagination(CursorPagination): 
        page_size = 3 
        ordering = 'name'   # default is 'created' - cursor pagination expects a created named tiemstamp field by default to order the result 
        cursor_query_param = 'navigate' # Default is cursor 
        