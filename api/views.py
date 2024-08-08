# views.py

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Response as ChatResponse
from .serializers import ResponseSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = ChatResponse.objects.all()
    serializer_class = ResponseSerializer

    @action(detail=False, methods=["get"])
    def suggestions(self, request):
        query = request.query_params.get("query", "").lower()
        if query:
            suggestions = ChatResponse.objects.filter(phrase__icontains=query)
        else:
            suggestions = []
        serializer = ResponseSerializer(suggestions, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def all_responses(self, request):
        responses = ChatResponse.objects.all()
        serializer = ResponseSerializer(responses, many=True)
        return Response(serializer.data)
