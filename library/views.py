from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .models import Categoría, Ingreso, Gasto
from .serializers import CategoríaSerializer, IngresoSerializer, GastoSerializer


class CategoriaViewset(viewsets.ModelViewSet):
    queryset = Categoría.objects.all()
    serializer_class = CategoríaSerializer

class IngresoViewset(viewsets.ModelViewSet):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer

class GastoViewset(viewsets.ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer


@api_view(['POST'])
def register(request):
    try:
        username = request.data['username']
        password = request.data['password']
        email = request.data.get('email', '')
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    except KeyError:
        return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
