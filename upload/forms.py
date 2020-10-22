from django import forms

from .models import File

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('title', 'author', 'file', 'cover')

class RenameForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('title',)
    
    def save(self, user=None):
        user_profile = super(RenameForm, self).save(commit=False)
        user_profile.save()
        return user_profile
