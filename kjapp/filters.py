from rest_framework.filters import BaseFilterBackend

class StartsWithFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        search = request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(name__icontains=search) | queryset.filter(phone__startswith=search) 
        return queryset