from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.settings import api_settings

from locales import models
from locales import permissions
from locales import serializers


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email',]
    ordering_fields = ['first_name', 'last_name', 'email']


class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ClasificacionesEmpresasViewSet(viewsets.ModelViewSet):
    """Maneja la lectura, creacion y actualizacion de las clasificaciones de empresas"""
    serializer_class = serializers.ClasificacionesEmpresasSerializer
    queryset = models.ClasificacionesEmpresas.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        IsAuthenticated,
    )
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['descripcion',]
    ordering_fields = ['descripcion']


class MedidasSanitariasViewSet(viewsets.ModelViewSet):
    """Maneja la lectura, creacion y actualizacion de las clasificaciones de empresas"""
    serializer_class = serializers.MedidasSanitariasSerializer
    queryset = models.MedidasSanitarias.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        IsAuthenticated,
    )
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['descripcion',]
    ordering_fields = ['descripcion']


class EmpresasViewSet(viewsets.ModelViewSet):
    """Maneja la lectura, creacion y actualizacion de las clasificaciones de empresas"""
    serializer_class = serializers.EmpresasSerializer

    queryset = models.Empresas.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        permissions.UpdateOwnBusiness,
    )
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['descripcion',]
    ordering_fields = ['descripcion']

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


class EmpresasMedidasViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.EmpresasMedidasSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = models.EmpresasMedidas.objects.all()
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )
    filter_backends = [filters.SearchFilter]
    search_fields = ['id_empresa',]

    # def list(self, request):
    #     empresa = self.request.query_params.get('empresa')
    #     queryset = models.EmpresasMedidas.objects.filter(id_empresa=empresa)
    #     return Response({'empresaMedidas': queryset})
