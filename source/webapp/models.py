from django.db import models


class Name(models.Model):
    name = models.CharField('Имя кота', max_length=200)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = 'Имена'