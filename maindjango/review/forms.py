from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['video_title', 'video_url','text','photo','rating']
        labels = {
            'video_title': 'Enter video name',
            'video_url': 'Enter video url',
            'text': 'Your Review',
            'photo': 'Upload an Image',
            'rating': 'Rate the Channel',
        }
        widgets = {
            'video_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title of the video',
                'maxlength': '255'
            }),
            'video_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the URL of the video'
            }),
            'text': forms.Textarea(attrs={
                'rows': 5,
                'class': 'form-control',
                'placeholder': 'Write your review here...'
            }),
            'rating': forms.Select(choices=Review.RATING_CHOICES, attrs={
                'class': 'form-control'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
        }