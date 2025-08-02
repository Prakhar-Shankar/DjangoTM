print("✅ Signals module loaded")

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task

@receiver(post_save, sender=Task)
def task_created_or_updated(sender, instance, created, **kwargs):
    if created:
        print(f"[Signal] ✅ New task created: {instance.title}")
    else:
        print(f"[Signal] 🛠 Task updated: {instance.title}")
