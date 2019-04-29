from django.conf.urls import url,include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter() #setting up a default router 
router.register('message-viewset',views.MessageViewSet, base_name='message-viewset')

urlpatterns = [
	url('',include(router.urls))
]