from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .serializers import WorkSerializer, ArtistSerializer
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User

class RegistrationAPIView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Please provide both username and password'}, status=400)

        user = User.objects.create_user(username=username, password=password)
        # token = Token.objects.create(user=user)
        return Response({'token': token.key}, status=201)
# Create your views here.
class WorkViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows work to be viewed or edited
    """
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Artist to be viewed or edited.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]