from django import forms
from .models import Jogo, Review


class JogoForm(forms.ModelForm):
    data_lancamento = forms.DateField(
        label='LANÇAMENTO',
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={'placeholder': 'dd/mm/aaaa'},
        ),
    )

    class Meta:
        model = Jogo
        fields = '__all__'
        widgets = {
            'plataformas': forms.CheckboxSelectMultiple,
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['autor', 'nota', 'comentario']