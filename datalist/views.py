from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Datalist
from .serializer import DatalistSerializer

def index(request):
    # datalists=[Datalist.objects.get(id=1),Datalist.objects.get(id=2)]
    datalists=Datalist.objects.all()
    return render(request,'index.html', {'datalists': datalists})



@api_view(['GET', 'POST'])
def data_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Datalist.objects.all()
        serializer = DatalistSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DatalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def data_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Datalist.objects.get(pk=pk)
    except Datalist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DatalistSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DatalistSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)