from django import forms

from comment.models import Comment


class CommentForm(forms.ModelForm):
    class Meta():
        # 指定该表单关联的数据库对象;
        model=Comment

        # 如果不指定， 数据库对象的每个属性都需要创建表单;
        # 如果指定fields, 只需要创建指定属性的表单;
        fields=['content']