from rest_framework import viewsets
from rest_framework.response import Response
from . import skin_ml
from .models import ApiSkin
from .serializers import ApiSkinSerializers


class ApiSkinView(viewsets.ModelViewSet):
    queryset = ApiSkin.objects.order_by("-id")
    serializer_class = ApiSkinSerializers

    def create(self, request, *args, **kwargs):
        viewsets.ModelViewSet.create(self, request, *args, **kwargs)
        json_object = ApiSkin.objects.latest("id")
        # grade = skin_ml.predict_skin(json_object.imagearray)
        return Response({json_object.imagearray})


