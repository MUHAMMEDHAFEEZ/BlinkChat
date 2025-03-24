from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
from .pusher import pusher_client

class MessageAPIView(APIView):
    def post(self, request):
        pusher_client.trigger('chat', 'message', {
            'username': request.data['username'],
            'message': request.data['message']
        })
        
        return Response([], status=status.HTTP_201_CREATED)

    def get(self, request):
        return Response([], status=status.HTTP_200_OK)

