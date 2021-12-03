from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import MenuItem
from .serializers import MenuItemSerializer

from django.db.models import Q
from functools import reduce, partial
import operator 


class MenuItemAPIView(APIView):
	# add item
	def post(self, request):
		try:
			items = request.data.get('items', '') 
			print(items, "itemsssssssssssssssssss")
			if items:
				for item in items:
					# name = item['name']
					# category = item['category']
					# subcategory = item['subcategory']
					# description = item['description']
					# price = item['price']
					print(item)
					# return 0
					serializer = MenuItemSerializer(data=item)
					if serializer.is_valid():
						serializer.save()
					else:
						print(serializer.errors)
						# raise Exception(serializer.errors)	
				return Response({"success": True, "message": "data saved successfully"})
			else:
				return Response({"success": False, "message": "Please enter item details"}, status=400)	
		except Exception as e:
			print(str(e))
			return Response({"success": False, "message": "Some error occurred please try again"})		

	def get(self, request):
		try:
			name = request.query_params.get('name', '')
			category = request.query_params.get('category', '')
			subcategory = request.query_params.get('subcategory', '')
			ans = name
			query_list = [Q(name__icontains=name), Q(category__icontains=category), Q(subcategory__icontains=subcategory)]
			qs = MenuItem.objects.filter(reduce(operator.and_, query_list))
			# print(qs)
			qs = MenuItemSerializer(qs, many=True)
			return Response({"success": True, "data": qs.data})		
		except Exception as e:
			print(str(e))	
			return Response({"success": False, "message": "Some error occurred please try again"})		
