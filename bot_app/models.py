from django.db import models


class User(models.Model):
    user_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username or str(self.user_id)

    class Meta:
        verbose_name = 'Телеграм пользователь'
        verbose_name_plural = 'Телеграм пользователи'


class Img(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Фото {self.id} пользователя {self.user}"

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
