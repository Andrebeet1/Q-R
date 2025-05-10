from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        widgets = {
            'question_text': forms.Textarea(attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Pose ta question ici...'}),
        }
