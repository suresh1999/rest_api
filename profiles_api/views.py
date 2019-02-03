from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):

	"""Test Api VIew """
	def get(self, request, format=None):
		"""Return a list of API feature"""

		an_apiview = [
			'Uses HTTP methods as functions(GET, POST, UPDATE, DELETE, PATCH)',
			'It is similar to a traditional django view',
			'Gives you the most control over your logic'
		]

		return Response({'message':'hello', 'an_api_view':an_apiview})
