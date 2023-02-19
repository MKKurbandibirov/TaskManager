from django.db import models
from .tag import Tag
from .user import User


class Task(models.Model):
    class State(models.TextChoices):
        NEW_TASK = "new_task"
        IN_DEV = "in_development"
        IN_QA = "in_qa"
        IN_CR = "in_code_review"
        READY_FOR_RELEASE = "ready_for_release"
        RELEASED = "released"
        ARCHIVED = "archived"

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    create_date = models.DateTimeField()
    change_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    priority = models.IntegerField()
    state = models.CharField(
        max_length=255, default=State.NEW_TASK, choices=State.choices
    )

    tags = models.ManyToManyField(Tag)

    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='author')
    manager = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='manager')
