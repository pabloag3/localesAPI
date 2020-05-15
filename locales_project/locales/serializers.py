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

    class Meta:
        model = models.Empresas
        fields = '__all__'
        extra_kwargs = {
            'user_profile': {'read_only': True},
            # 'id_clasificacion_empresa': {'read_only': True}
        }


class EmpresasMedidasSerializer(serializers.ModelSerializer):
    """Serializar las medidas y las empresas en conjunto"""

    class Meta:
        model = models.EmpresasMedidas
        fields = '__all__'
