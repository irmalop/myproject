from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from app1.serializers import PersonSerializer
from app1.models import Person
from django.views.decorators.clickjacking import xframe_options_exempt
@api_view(['GET'])
def hello(request, name):
    return Response({'message':f'Hello {name}'}, status=status.HTTP_200_OK)

class  PersonListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        person_list = Person.objects.filter(status=True)
        serializer=PersonSerializer(person_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class  PersonCreateAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self, request):
        serializer=PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class  PersonRetrieveUpdateDeleteAPIView(APIView):
    permission_classes = (AllowAny, )
    def get(self, request,pk):
        person_obj=get_object_or_404(Person,pk=pk)
        serializer=PersonSerializer(person_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request,pk):
        person_obj=get_object_or_404(Person,pk=pk)
        serializer=PersonSerializer(person_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request,pk):
        person_obj=get_object_or_404(Person,pk=pk)
        person_obj.status=False
        person_obj.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

### ---modelview sets ---###
class  PersonViewSet(ModelViewSet):
    permission_classes = (AllowAny, )
    serializer_class = PersonSerializer
    queryset = ''
    