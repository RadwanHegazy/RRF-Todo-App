from django.db import models
from django.contrib.auth.models import User

class Todo (models.Model) : 
    user = models.ForeignKey(User, related_name='user_todo',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=250)
    is_done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text
