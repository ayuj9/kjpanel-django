from .models import Client , Address , Client_Plan ,Client_Insights , Diet_Plan , RecipeData
from rest_framework import serializers
from django.utils import timezone


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model =Address
        fields = ['country' ]


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_Plan
        fields = ['id','plan_level','duration', 'status' ,'start_time' , 'end_time' , 'client' ]  
        read_only_fields = ('client',)         

class Client_InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_Insights
        fields=['id' ,'height' , 'current_weight'   , 'client' ]

        # def update(self , instance , )




class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id' , 'city' , 'state' , 'country' , 'client']    
        read_only_fields = ('client',)    

    def update(self, instance, validated_data):
        instance.country = validated_data.get('country', instance.country)
        instance.state = validated_data.get('state', instance.state)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

class ClientSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


# class Diet_PlanSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =  Diet_Plan
#         fields= [ 'id' , 'day1','day2','day3','day4','day5' , 'day6' , 'day7' , 'client'  ]   


class Diet_PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet_Plan
        fields = ['id', 'day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7', 'time', 'client','note']
        # read_only_fields = ['client']

    def update(self, instance, validated_data):
        instance.day1 = validated_data.get('day1', instance.day1)
        instance.day2 = validated_data.get('day2', instance.day2)
        instance.day3 = validated_data.get('day3', instance.day3)
        instance.day4 = validated_data.get('day4', instance.day4)
        instance.day5 = validated_data.get('day5', instance.day5)
        instance.day6 = validated_data.get('day6', instance.day6)
        instance.day7 = validated_data.get('day7', instance.day7)
        instance.time = validated_data.get('time', instance.time)
        instance.save()
        return instance

# class ClientDietSerializer(serializers.ModelSerializer):
#     id = serializers.UUIDField(read_only = True)
#     diet = Diet_PlanSerializer();

#     class Meta:
#         model = Diet_Plan
#         fields = ['id' ,'diet' ]

    


class Client_PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_Plan
        fields= ['id' , 'plan_level' ,'duration' , 'start_time' , 'end_time' , 'status'   , 'client']
        read_only_fields = ('client',)
    def update(self, instance, validated_data):
        # validated_data['last_plan_updated_timestamp'] = timezone.now()
        instance.status = validated_data.get('status' , instance.status)
        instance.save()
        return instance
        # return super().update(instance, validated_data)



class StatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_Plan
        fields = ['status']


class Member_ListSerializer(serializers.ModelSerializer):
    address  = CountrySerializer();
    plan = PlanSerializer(many=True);
    
    class Meta:
        model = Client
        fields=['id' , 'name' , 'phone', 'address' , 'plan' ,'diet_preference' ]   



    

class Insights_FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_Insights
        fields = ['id' ,'height' , 'current_weight' ,'target_weight' , 'client' ,'persona', 'height_Unit', 'weight_Unit']
        read_only_fields = ('client',)

    def update(self , instance , validated_data):
        instance.height = validated_data.get('height' , instance.height)    
        instance.current_weight = validated_data.get('current_weight' , instance.current_weight)    
        instance.target_weight = validated_data.get('target_weight' , instance.target_weight)    
        instance.save()
        return instance


class Client_All_DetailsSerializer(serializers.ModelSerializer):
    insights = Insights_FormSerializer(many=True);
    address = AddressSerializer();
    plan = PlanSerializer(many =True);
    class Meta:
        model = Client
        fields = ['id' , 'name' , 'age' , 'gender' , 'phone' , 'note',
                   'email'  , 'diet_preference' , 'file',
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
    
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields= ['file'] 
        

class TimeUpdateSerializr(serializers.ModelSerializer):
    class Meta:
        model = Client_Plan
        fields = ['start_time' , 'end_time']            
    
    
    
class AddNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet_Plan
        fields = ['note']
        


class SearchRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeData
        fields = ['id' , 'name' , 'recipieLink']

class ClientNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id' , 'name' , 'phone']        
