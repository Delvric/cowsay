from django.db import models


class CowInput(models.Model):
    cowfield = models.CharField(max_length=80)

    def __str__(self):
        return self.cowfield
