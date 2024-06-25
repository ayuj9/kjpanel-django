from rest_framework.filters import BaseFilterBackend

class StartsWithFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        phone = request.query_params.get('phone', None)
        if phone:
            queryset = queryset.filter(phone__startswith=phone)
        return queryset