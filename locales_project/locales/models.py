from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings

import datetime


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, first_name, last_name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('El usuario debe tener un correo.')
        if not first_name:
            raise ValueError('El usuario debe tener un nombre.')
        if not last_name:
            raise ValueError('El usuario debe tener un apellido.')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, first_name, last_name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=datetime.datetime.now)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name', 'password']

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.first_name + ' ' + self.last_name 

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.first_name

    def __str__(self):
        """Return string representation of user"""
        return self.email


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Empresas(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    descripcion = models.CharField(max_length=50)
    direccion = models.CharField(max_length=300)
    longitud = models.CharField(max_length=20, blank=True, null=True)
    latitud = models.CharField(max_length=20, blank=True, null=True)
    id_clasificacion_empresa = models.ForeignKey('ClasificacionesEmpresas', models.DO_NOTHING, db_column='id_clasificacion_empresa')

    class Meta:
        managed = False
        db_table = 'empresas'
    
    def __str__(self):
        """Return the model as a string"""
        return self.descripcion


class EmpresasMedidas(models.Model):
    cod_empresa_medida = models.AutoField(primary_key=True)
    id_medida_sanitaria = models.ForeignKey('MedidasSanitarias', models.DO_NOTHING, db_column='id_medida_sanitaria')
    id_empresa = models.ForeignKey('Empresas', models.DO_NOTHING, db_column='id_empresa')

    class Meta:
        managed = False
        db_table = 'empresas_medidas'


class ClasificacionesEmpresas(models.Model):
    id_clasificacion_empresa = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'clasificaciones_empresas'
    

    def __str__(self):
        """Return the model as a string"""
        # return self.descripcion
        return self.descripcion


class MedidasSanitarias(models.Model):
    id_medida_sanitaria = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'medidas_sanitarias'
    
    def __str__(self):
        """Return the model as a string"""
        return self.descripcion
