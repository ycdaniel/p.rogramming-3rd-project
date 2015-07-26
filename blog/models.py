from django.core.files import File
from django.db import models
from django.db.models.signals import pre_save
from blog.utils import random_name_upload_to
from blog.utils import square_image, thumbnail


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True,
                              upload_to=random_name_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def pre_on_post_save(sender, **kwargs):
    post = kwargs['instance']
    if post.image:
        max_width = 300
        if post.image.width > max_width or post.image.height > max_width:
            processed_file = thumbnail(post.image.file, max_width, max_width)
            # processed_file = square_image(post.image.file, max_width)
            post.image.save(post.image.name, File(processed_file))

pre_save.connect(pre_on_post_save, sender=Post)
