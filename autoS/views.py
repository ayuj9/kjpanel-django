from django.shortcuts import render
from .models import Names ,ProductImage
import json
from django.core.mail import EmailMessage , BadHeaderError
from rest_framework.viewsets import ModelViewSet
from .serializers import ImageSerializer


# Create your views here.

def index(request):
    return render(request , 'index.html')

def check(request):
    try:
        mess = EmailMessage('subject' ,'message' ,'info@moshbuy.com' , ['bob@moshbuy.com '])
        mess.attach_file('autoS/static/images/dog.jpg')
        mess.send()
    except BadHeaderError:
        pass    
    return render(request , 'index.html')




def import_data(request):
    if request.method == 'POST' and request.FILES['json_file']:
        json_file = request.FILES['json_file']
        data = json.load(json_file)    

        print(data.type())
        for i in range(1,813):
            print(data[str(0)]['RecipieLink'])
            # recipeLink = data[str(i)]['RecipieLink']
            # recipeLink1 = data[str(i)]['RecipieLink_1']
            # print(i , recipeLnk1)
            # recipeL = recipeLink
            # if recipeLink == 'None':
            #     recipeL = recipeLink1
            # else :
            #     recipeL = recipeLink    
           
            print(data[1]['id'])
            names = Names(
                id = data[i]['id'] , # Accessing data with str(i) as key
                name = data[i]["name"],
                recipieLink  = data[i]['recipieLink']  # Adjust for correct key name
            )
            names.save()
        return render(request, 'index.html')
    return render(request, 'index.html')



class ProductImageViewSet(ModelViewSet):
    serializer_class = ImageSerializer
    queryset = ProductImage.objects.all()

    def get_queryset(self):
        return ProductImage.objects.filter(product_id =self.kwargs['product_pk '] )

    

