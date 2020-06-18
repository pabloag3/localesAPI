from rest_framework import serializers
from locales import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )

        return user


class ClasificacionesEmpresasSerializer(serializers.ModelSerializer):
    """Serializar las clasificaciones de empresas"""

    class Meta:
        model = models.ClasificacionesEmpresas
        fields = '__all__'


class MedidasSanitariasSerializer(serializers.ModelSerializer):
    """Serializar las medidas sanitarias"""

    class Meta:
        model = models.MedidasSanitarias
        fields = '__all__'


class EmpresasSerializer(serializers.ModelSerializer):
    """Serializar las empresas"""

    clasificacion_empresa = serializers.SerializerMethodField()

    class Meta:
        model = models.Empresas
        fields =  ['id_empresa', 'descripcion', 'direccion', 'longitud', 'latitud', 'id_clasificacion_empresa', 'clasificacion_empresa']
        extra_kwargs = {
            'user_profile': {'read_only': True},
        }
    
    def get_clasificacion_empresa(self, obj):
        return obj.id_clasificacion_empresa.descripcion


class EmpresasMedidasSerializer(serializers.ModelSerializer):
    """Serializar las medidas y las empresas en conjunto"""

    medida_sanitaria = serializers.SerializerMethodField()

    class Meta:
        model = models.EmpresasMedidas
        fields = '__all__'

    def get_medida_sanitaria(self, obj):
        return obj.id_medida_sanitaria.descripcion
