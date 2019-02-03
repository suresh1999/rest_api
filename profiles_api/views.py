from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status


# Create your views here.

class HelloApiView(APIView):

	"""Test Api VIew """

	serializer_class = serializers.HelloSerializer
	def get(self, request, format=None):
		"""Return a list of API feature"""

		an_apiview = [
			'Uses HTTP methods as functions(GET, POST, UPDATE, DELETE, PATCH)',
			'It is similar to a traditional django view',
			'Gives you the most control over your logic'
		]

		return Response({'message':'hello', 'an_api_view':an_apiview})


	def post(self, request):

		serializer = serializers.HelloSerializer(data=request.POST)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message':message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk=None):
		"""Handles updating an object"""

		return Response({'method':'put'})

	def patch(self, request, pk=None):

		return Response({'method':'patch'})

	def delete(self, request, pk=None):
		return Response({'method' : 'delete'})
