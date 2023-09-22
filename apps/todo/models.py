from django.db import models

class ToDo(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название таска'
    )
    description = models.CharField(
        max_length=100,
        verbose_name='Описание'
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name='Статус операции'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано'
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Таск"
        verbose_name_plural = "Таски"