from rest_framework import serializers
from .models import ApiSkin


class ApiSkinSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiSkin
        fields = '__all__'
