from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .serializers import WorkSerializer, ArtistSerializer, UserSerializer
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from .models import Client, Artist, Work
from rest_framework.response import Response

class RegistrationAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Please provide both username and password'}, status=400)

        # create a new User object
        user = User.objects.create_user(username=username, password=password)

        # create a new Client object associated with the new User object
        client = Client.objects.create(user=user, name=username)

        return Response(status=201)


class ClientViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Client.objects.all()
    serializer_class = UserSerializer


class WorkViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows work to be viewed or edited
    """
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Work.objects.all()
        artist = self.request.query_params.get('artist')
        work_type = self.request.query_params.get('work_type')

        if artist:
            queryset = queryset.filter(artist__name=artist)

        if work_type:
            queryset = queryset.filter(work_type__icontains=work_type)

        return queryset


class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Artist to be viewed or edited.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # permission_classes = [permissions.IsAuthenticated]