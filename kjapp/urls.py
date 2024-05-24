from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('client', views.CLientViewSet)
router.register('address' , views.AddressViewSet)
router.register('plan' , views.ClientPlanViewSet)
router.register('Insights' , views.InsightViewSet)
router.register('diet_plan' , views.DietPlanViewSet)
router.register('member_list' , views.MemberListViewSet, basename='member-list')
router.register('clientAllDetail', views.CLientAllDetailsViewSet , basename='all-detail')

urlpatterns = router.urls

# urlpatterns=[
#     # path('/' , include(router.urls)),
#     path('client/' , views.CLientViewSet.as_view() )
# ]\\\