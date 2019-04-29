from django.shortcuts import render

from rest_framework import viewsets 
from rest_framework.response import Response

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken



class MessageViewSet(viewsets.ViewSet): #A simple viewset to tell the aim of this api/project
	
	def list(self, request):

		objective = [
			'The problem statement is',
			'An api in which a user cant access another users data/profile',
			'Eg:~ user with profile id 7 should be able to access /api/profile/7/ but not /api/profile/8/'
		]

		return Response({'Message': 'Welcome!', 'Objective': objective})


class LoginViewSet(viewsets.ViewSet): #Checks email and password and returns an auth token.

	serializer_class = AuthTokenSerializer

	def create(self, request): #using ObtainAuthToken APIView to validate and create a token.

		return ObtainAuthToken().post(request)
