from django.urls import path, include
from rest_framework import routers

from linkedin.views import SearchViewSet, JobPostViewSet, CompanyViewSet, TrackingViewSet

router = routers.DefaultRouter()
router.register('search', SearchViewSet)
router.register('jobs', JobPostViewSet)
router.register('companies', CompanyViewSet)
router.register('tracking', TrackingViewSet)

urlpatterns = [
    path('', include(router.urls))
]
