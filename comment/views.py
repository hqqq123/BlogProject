from django.http import request
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse

from blog.models import Post
from comment.forms import CommentForm


def post_comment(request,id):
    post=get_object_or_404(Post,id=id)
    user=request.user
    if request.method=='POST':
        form =CommentForm(request.POST)
        if(form.is_valid()):
            comment=form.save(commit=False)
            comment.post=post
            comment.user=user

            post.comment_num+=1
            comment.save()
            post.save()

        return redirect(reverse('detail',kwargs={'id':post.id}))