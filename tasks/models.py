from users.models import User_model
from django.db import models
from django.utils.text import slugify

import uuid

class TaskModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    slug = models.SlugField(max_length=64, blank=True, editable=False, unique=True)
    summary = models.CharField(max_length=64)
    description = models.TextField()
    completed = models.BooleanField(verbose_name='Task completed', default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    assignee = models.ForeignKey('users.User_model', on_delete=models.PROTECT, blank=True, null=True, related_name='assignee')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_slug': self.slug})
