from django.urls import path, include

from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')
router.register('profile', UserProfileViewSet)
router.register('login', LoginViewSet, base_name="login-viewset")
router.register('feed', UserProfileFeedViewSet)

urlpatterns = [
	path('hello-view/', HelloApiView.as_view()),
	path('', include(router.urls))
]