from functools import partial
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from lib_app.models import Book
from lib_app.serializers import Bookserializer

class LibraryView(APIView):
    def get(self,request,pk=None):

        if pk:
            books = Book.objects.get(book_id=pk)
            serializer = Bookserializer(books)
            return Response({"status":200, "data" :serializer.data})

        books = Book.objects.all()
        serializer = Bookserializer(books, many=True)
        return Response({"status":200, "data" :serializer.data})
        

    def post(self,request):

        serializer = Bookserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)


    def put(self,request, pk=None):
        books = Book.objects.get(book_id=pk)

        serializer_class = Bookserializer(books,data=request.data,partial=True)
        if serializer_class.is_valid():
            
            serializer_class.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer_class.errors)


    def delete(self,request,pk=None):
        if pk:
            books = Book.objects.get(id=pk)
            books.delete()
            return Response({'msg':'Data Deleted'})

        return Response({'msg':'Please provide book id'})   

    
