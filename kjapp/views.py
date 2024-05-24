from django.shortcuts import render
from django.http import HttpResponse 
# from rest_framework.mixins import CreateModelMixin , RetrieveModelMixin , DestroyModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Client , Address , Client_Plan , Client_Insights , Diet_Plan
from  .serializers import ClientSerailizer , AddressSerializer , Client_PlanSerializer , Client_InsightSerializer , Diet_PlanSerializer , Member_ListSerializer , Client_All_DetailsSerializer


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
    serializer_class = Client_InsightSerializer


class DietPlanViewSet(ModelViewSet):
    queryset = Diet_Plan.objects.all()
    serializer_class = Diet_PlanSerializer 


class MemberListViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = Member_ListSerializer 


class CLientAllDetailsViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = Client_All_DetailsSerializer
    
            

   
   

