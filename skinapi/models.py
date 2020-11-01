
from django.db import models


class ApiSkin(models.Model):
    imagearray = models.TextField()

    def take_string(self):
        return {
            'imagearray': self.imagearray
        }
