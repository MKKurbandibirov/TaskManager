from django.db import models
from models import tag, user


class Task(models.Model):
    class State(models.TextChoices):
        NEW_TASK = "new_task"
        IN_DEV = "in_development"
        IN_QA = "in_qa"
        IN_CR = "in_code_review"
        READY_FOR_RELEASE = "ready_for_release"
        RELEASED = "released"
        ARCHIVED = "archived"

    title = models.CharField(max_length=63)
    description = models.CharField(max_length=255)
    create_date = models.DateTimeField()
    change_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    priority = models.IntegerField()
    tags = models.ManyToManyField(tag.Tag)
    author = models.ForeignKey(user.User, on_delete=models.CASCADE)
    manager = models.ForeignKey(user.User, on_delete=models.CASCADE)
    state = models.CharField(
        max_length=63, default=State.NEW_TASK, choices=State.choices
    )
