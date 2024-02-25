from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import userLogin,Entries
from django.http import JsonResponse
from .serializers import userSerializer,entrySerializer
from rest_framework.response import Response
from web3 import Web3,HTTPProvider

# Create your views here.

@api_view(['GET'])
def demo(request):
    people=userLogin.objects.all()
    serializer=userSerializer(people,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def entries(request,pk):
    person=userLogin.objects.get(id=pk)
    entry=Entries.objects.all()
    print(entry)
    serializer=entrySerializer(entry,many=True)
    print(serializer.data)
    return Response(serializer.data)

# @api_view(['GET'])
# def test(request):
#     infura_url="https://mainnet.infura.io/v3/ab7852ae752e4bf0b4ffb82ada79e49c"
#     web3=Web3(Web3.HTTPProvider(infura_url))
#     print(is_connected(web3))
#     return JsonResponse(web3.isConnected(),safe=False)
    

