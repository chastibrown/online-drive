from django.db import models
from django.contrib.auth import get_user_model


class File(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
                            get_user_model(),
                            on_delete=models.CASCADE,
                                )
    file = models.FileField(upload_to='drive/file/')
    cover = models.ImageField(upload_to='file/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
