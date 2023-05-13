from asyncio import format_helpers

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
from django.db import models
from tinymce import models as tinymce_model


class Blog(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="thumbnails")
    description = models.TextField()
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def semantic_autocomplete(self):
        html = self.get_img()
        return format_helpers(html)

    def __str__(self) -> str:
        return f"Blog title-{self.title} written on {self.created_at.date()}"
