from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import filters
from rest_framework import generics

from locales import serializers
from locales import models
from locales import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filters_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'email',)


class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ClasificacionesEmpresasViewSet(viewsets.ModelViewSet):
    """Maneja la lectura, creacion y actualizacion de las clasificaciones de empresas"""
    serializer_class = serializers.ClasificacionesEmpresasSerializer
    queryset = models.ClasificacionesEmpresas.objects.all()
    authentication_classes = (TokenAuthentication,)
    filters_backends = (filters.SearchFilter,)
    permission_classes = (
        IsAuthenticated,
    )
    search_fields = ('descripcion',)


class MedidasSanitariasViewSet(viewsets.ModelViewSet):
    """Maneja la lectura, creacion y actualizacion de las clasificaciones de empresas"""
    serializer_class = serializers.MedidasSanitariasSerializer
    queryset = models.MedidasSanitarias.objects.all()
    authentication_classes = (TokenAuthentication,)
    filters_backends = (filters.SearchFilter,)
    permission_classes = (
        IsAuthenticated,
    )
    search_fields = ('descripcion',)


class EmpresasViewSet(viewsets.ModelViewSet):
    """Maneja la lectura, creacion y actualizacion de las clasificaciones de empresas"""
    serializer_class = serializers.EmpresasSerializer

    queryset = models.Empresas.objects.all()
    authentication_classes = (TokenAuthentication,)
    filters_backends = (filters.SearchFilter,)
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        permissions.UpdateOwnBusiness,
    )
    search_fields = ('descripcion',)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
