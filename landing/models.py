from django.db import models


class Subscribers(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Id: %s, Login: %s' % (self.name, self.email,)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'