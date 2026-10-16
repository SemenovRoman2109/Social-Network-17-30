from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random
# Create your models here

class VerifyCode(models.Model):
    code = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='verify_code')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def generate_code(self):
        self.code = str(random.randint(100000, 999999))
        self.created_at = timezone.now()
        self.save()

    def is_valid(self):
        delta = timezone.now() - self.created_at
        if delta.total_seconds() < (5 * 60):
            return True
        return False
        
    