from django import forms

from rest_framework.exceptions import ValidationError

from .models import Follow


class FollowForm(forms.ModelForm):
    model = Follow

    def clean(self):
        if self.user == self.author:
            raise ValidationError('Нельзя подписаться на самого себя!')
