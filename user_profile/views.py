from django.shortcuts import render

from rest_framework import viewsets 
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.permissions import AllowAny

from . import serializers
from . import models
from . permissions import IsAdminUser, IsLoggedInUserOrAdmin


class MessageViewSet(viewsets.ViewSet): #A simple viewset to tell the aim of this api/project
	
	def list(self, request):

		objective = [
			'The problem statement is',
			'An api in which a user cant access another users data/profile',
			'Eg:~ user with profile id 7 should be able to access /api/profile/7/ but not /api/profile/8/'
		]

		return Response({'Message': 'Welcome!', 'Objective': objective})


class UserProfileViewSet(viewsets.ModelViewSet): #Handles creating,reading and updating profiles.ModelViewSet of djangorestframework takes care of all the logic for creating,reading and updating model items(really useful for simple apis)

	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all() #queryset tells the viewset how to retrieve the objects from database i,e from which model.
	authentication_classes = (TokenAuthentication,)

	def get_permissions(self):
		permission_classes = []
		if self.action == 'create': #so that anyone can create an account
			permission_classes = [AllowAny]
		elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update': #i.e to get a specific users details i.e api/profile/2 (LOGGED in user can only view and update his own profile.)
			permission_classes = [IsLoggedInUserOrAdmin]
		elif self.action == 'list' or self.action == 'destroy': #Only admin/superuser has permission to see all users in list 
			permission_classes = [IsAdminUser]
		return [permission() for permission in permission_classes]


class LoginViewSet(viewsets.ViewSet): #Checks email and password and returns an auth token.

	serializer_class = AuthTokenSerializer

	def create(self, request): #using ObtainAuthToken APIView to validate and create a token.

		return ObtainAuthToken().post(request)
