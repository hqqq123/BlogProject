from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Comment(models.Model):
    content=models.TextField(verbose_name="评论内容")
    created_time = models.DateTimeField(auto_now=True,verbose_name="评论时间")
    post=models.ForeignKey('blog.Post',on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.content[:30]

