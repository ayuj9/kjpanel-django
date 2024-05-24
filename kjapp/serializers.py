from .models import Client , Address , Client_Plan ,Client_Insights , Diet_Plan
from rest_framework import serializers
from django.utils import timezone


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model =Address
        fields = ['country' ]


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_Plan
        fields = ['id','plan_level', 'status' ,'start_time' , 'end_time' ,'target_weight', 'client' ]  
        read_only_fields = ('client',)         

class Client_InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_Insights
        fields=['id' ,'height' , 'current_weight' , 'note'  , 'client' ]

        # def update(self , instance , )

class Diet_PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Diet_Plan
        fields= [ 'id' , 'day1','day2','day3','day4','day5' , 'day6' , 'day7' , 'client' ]   


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id' , 'city' , 'state' , 'country' , 'client']    
        read_only_fields = ('client',)    

class ClientSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id' , 'name' , 'age' , 'gender' , 'phone' ,
                   'email'  , 'diet_preference' ,
                  'diet_language' ]
        




class Client_PlanSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        validated_data['last_plan_updated_timestamp'] = timezone.now()
        return super().update(instance, validated_data)

    class Meta:
        model = Client_Plan
        fields= ['id' , 'plan_level' , 'start_time' , 'end_time' , 'status' , 'target_weight'  , 'client']


class Member_ListSerializer(serializers.ModelSerializer):
    address  = CountrySerializer();
    plan = PlanSerializer(many=True);
    
    class Meta:
        model = Client
        fields=['id' , 'name' , 'phone', 'address' , 'plan']   

class Insights_FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_Insights
        fields = ['id' ,'height' , 'current_weight' , 'note' , 'client' ,'persona', 'height_Unit', 'weight_Unit']
        read_only_fields = ('client',)


class Client_All_DetailsSerializer(serializers.ModelSerializer):
    insights = Insights_FormSerializer(many=True);
    address = AddressSerializer();
    plan = PlanSerializer(many =True);
    class Meta:
        model = Client
        fields = ['id' , 'name' , 'age' , 'gender' , 'phone' ,
                   'email'  , 'diet_preference' ,
                  'diet_language'  , 'address' , 'insights'  , 'plan']
        
    
    def create(self , validated_data):
        insights =validated_data.pop('insights')
        plan =validated_data.pop('plan')
        address_data =validated_data.pop('address')
        client = Client.objects.create( **validated_data)
        
        address = Address.objects.create(client = client , **address_data)

        for val in insights:
            Client_Insights.objects.create(**val ,client =  client )

        for val in plan:
            Client_Plan.objects.create(**val ,client =  client )

        return client
    

