from rest_framework import serializers
from .models import Leaf
from .models import UserRegister
from .models import PlantImage
from .models import Disease

class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = ('id', 'image')
        
        
class LeafSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaf
        fields = ['shape', 'color', 'size']

    extra_kwargs = {
        'observed_date': {'required': False}
    }


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = ['id', 'name', 'email', 'password', 'uniqueId', 'rememberMe']


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ['id', 'imageName', 'diseaseName', 'details']