from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "per"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(OrderedDict({
            "pagination": {
                "count": len(data),
                "next": self.page.next_page_number() if self.page.has_next() else None,
                "total_count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "current_page": self.page.number,
            },
            "result": data,
        }))

    def get_paginated_response_schema(self, schema):
        return {
            "type": "object",
            "properties": {
                "count": {
                    "type": "integer",
                },
                "next": {
                    "type": "boolean",
                    "nullable": True,
                },
                "total_count": {
                    "type": "integer",
                },
                "total_pages": {
                    "type": "integer",
                },
                "current_page": {
                    "type": "integer",
                },
                "result": schema,
            },
        }
