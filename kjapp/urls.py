from django.urls import path , include
from . import views
from rest_framework_nested import routers  
from django.conf import settings
from django.conf.urls.static import static



router = routers.DefaultRouter()
# router.register(r'admin' , admin.site.urls)
router.register('client', views.CLientViewSet )
router.register('address' , views.AddressViewSet)
router.register('plan' , views.ClientPlanViewSet)
router.register('insights' , views.InsightViewSet)
router.register('recipe' , views.SearchRecipeViewSet )
router.register('dietPlan' , views.DietPlanViewSet ,basename='client-diet')
router.register('count' , views.CountDownViewSet , basename = 'count')
router.register('member_list' , views.MemberListViewSet, basename='member-list')
router.register('clientAllDetail', views.CLientAllDetailsViewSet , basename='all-detail')
router.register('statusUpdate', views.StatusUpdateViewSet , basename='Update-status')
router.register('timeUpdate', views.TimeUpdateViewSet , basename='time-update')
router.register('note' , views.NoteViewSet , basename='add-note')
router.register('clientName' , views.ClientNameViewSet , basename='client-name')
router.register('mealTime' , views.MealTimeViewSet , basename='meal-time')
router.register('measures', views.MeasureDetailsViewSet , basename='measure-details')
router.register('zone' , views.ZoneViewSet , basename='zone-time')
# router.register('ImportRecipe' , views.import_data , basename='import-recipe')


clients_router =routers.NestedSimpleRouter(router , r'client' , lookup='client_pk')
clients_router.register(r'diet_plan/(?P<date>\d{4}-\d{1,2}-\d{1,2})' , views.ClientDietPlanViewSet , basename='client-dietplan')
clients_router.register(r'file' , views.FileUploadViewSet , basename='client-file')


urlpatterns=[
    path('importData/' , views.import_data )
]

urlpatterns += router.urls + clients_router.urls

# Add static files in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    