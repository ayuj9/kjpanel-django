from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('' , views.import_data )
]

# router = routers.DefaultRouter()
# router.register('import', views.import_data )
# router.register('mail', views.check )
# router.register('images' , views.ProductImageViewSet , basename ='product-image')



# if settings.DEBUG :
#     urlpatterns = router.urls  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    