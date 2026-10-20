from django import forms
from .models import Jogo, Review


class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = '__all__'
        widgets = {
            'data_lancamento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'plataformas': forms.CheckboxSelectMultiple,
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['autor', 'nota', 'comentario']