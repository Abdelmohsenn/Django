from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics
# Create your views here.
from .models import BankAccount
from .serializers import BankAccountSerializer

class BankAccountList(APIView):
    def get(self, request):
        bank_accounts = BankAccount.objects.all()
        serializer = BankAccountSerializer(bank_accounts, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = BankAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
