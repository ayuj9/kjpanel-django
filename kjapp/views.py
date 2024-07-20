from django.shortcuts import render
from django.http import HttpResponse 
from rest_framework.viewsets import ModelViewSet , GenericViewSet
from rest_framework.filters import SearchFilter
from .models import Client , Address , Client_Plan , Client_Insights , Diet_Plan ,RecipeData , FileUpload
from  .serializers import ClientSerailizer , AddressSerializer , Client_PlanSerializer , Client_InsightSerializer , Diet_PlanSerializer , Member_ListSerializer , Client_All_DetailsSerializer , Insights_FormSerializer,StatusUpdateSerializer, FileSerializer, TimeUpdateSerializr , AddNoteSerializer , SearchRecipeSerializer ,ClientNameSerializer , MealTimeSerializer , CountDownSerializer , TimeZoneSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from  rest_framework.mixins import CreateModelMixin,RetrieveModelMixin
from .filters import StartsWithFilterBackend
from rest_framework import status
from django.utils import timezone
import pytz 

# Create your views here.

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer   

    def get_serializer_context(self):
        return {'request':self.request}

class CLientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerailizer


class ClientPlanViewSet(ModelViewSet):
    queryset = Client_Plan.objects.all()
    serializer_class = Client_PlanSerializer

class InsightViewSet(ModelViewSet):
    queryset = Client_Insights.objects.all()
    serializer_class = Insights_FormSerializer


class MeasureDetailsViewSet(ModelViewSet):
    queryset = Client_Insights.objects.all()
    serializer_class = Client_InsightSerializer


class MemberListViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = Member_ListSerializer 


class CLientAllDetailsViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = Client_All_DetailsSerializer


class StatusUpdateViewSet(ModelViewSet):
    queryset = Client_Plan.objects.all()
    serializer_class = StatusUpdateSerializer 

class CountDownViewSet(ModelViewSet):
    queryset = Client_Plan.objects.all()
    serializer_class = CountDownSerializer

class TimeUpdateViewSet(ModelViewSet):
    queryset = Client_Plan.objects.all()    
    serializer_class = TimeUpdateSerializr

# class FileUploadViewSet(ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = FileSerializer
#     parser_classes = (MultiPartParser, FormParser)




#     def update(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileUploadViewSet(ModelViewSet):
    serializer_class = FileSerializer
    

    def get_serializer_context(self):
        return {'client_id':self.kwargs['client_pk__pk']}


    def get_queryset(self):
        client_id = self.kwargs.get("client_pk__pk")
        print(client_id)
        
        # return FileUpload.objects.filter(client_id )


class DietPlanViewSet(ModelViewSet , CreateModelMixin):
    queryset = Diet_Plan.objects.all()
    serializer_class =  Diet_PlanSerializer    
    
# class ClientDietPlanViewSet(ModelViewSet):
#     serializer_class = Diet_PlanSerializer
    
#     def get_queryset(self):
#         return Diet_Plan.objects.filter(client = self.kwargs['client_pk'])
    

class ClientDietPlanViewSet(ModelViewSet):
    serializer_class = Diet_PlanSerializer

    def get_queryset(self , *args, **kwargs):
        return Diet_Plan.objects.filter(client_id=self.kwargs["client_pk__pk"])
        

    def perform_create(self,  serializer):
        
        client_id = self.kwargs.get("client_pk__pk")
        client = Client.objects.get(pk=client_id)
        serializer.save(client=client)

    
   
class NoteViewSet(ModelViewSet):
    serializer_class = AddNoteSerializer
    queryset = Diet_Plan.objects.all()
   
class MealTimeViewSet(ModelViewSet):
    serializer_class = MealTimeSerializer
    queryset = Diet_Plan.objects.all()


class SearchRecipeViewSet(ModelViewSet):
    queryset = RecipeData.objects.all()
    serializer_class = SearchRecipeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

  


class ClientNameViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientNameSerializer
    filter_backends = [SearchFilter , StartsWithFilterBackend]
    search_fields = ['name','phone' ]


class ZoneViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = TimeZoneSerializer
   
    

    
