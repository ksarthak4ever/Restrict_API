from django.shortcuts import render

from rest_framework import viewsets 
from rest_framework.response import Response



class MessageViewSet(viewsets.ViewSet): #A simple viewset to tell the aim of this api/project
	
	def list(self, request):

		objective = [
			'The problem statement is',
			'An api in which a user cant access another users data/profile',
			'Eg:~ user with profile id 7 should be able to access /api/profile/7/ but not /api/profile/8/'
		]

		return Response({'Message': 'Welcome!', 'Objective': objective})
