from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text','photo','rating']
        labels = {
            'text': 'Your Review',
            'photo': 'Upload an Image',
            'rating': 'Rate the Channel',
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your review here...'}),
            'rating': forms.Select(choices=Review.RATING_CHOICES),
        }