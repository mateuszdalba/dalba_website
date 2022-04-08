from django.db import models
import random




class Motto(models.Model):
    text = models.TextField()

    @property
    def get_random(self):
        mottos_pks = list(Motto.objects.values_list('id', flat=True))
        pk = random.choice(mottos_pks)
        motto = Motto.objects.get(pk=pk)
        return motto

    def __str__(self):
        return self.text