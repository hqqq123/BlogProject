from django.urls import path

from comment.views import post_comment

urlpatterns = [
    path('post/<int:id>/', post_comment, name='post_comment'),

]