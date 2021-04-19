from django import forms
from movies.models import Reviews, Rating, RatingStar


class ReviewFrom(forms.ModelForm):
	'''Форма отзывов'''
	class Meta:
		model = Reviews
		fields = ('name', 'email', 'text', 'parent')


class RatingForm(forms.ModelForm):
	'''Форма добавления рейтинга'''
	tar = forms.ModelChoiceField(
		queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
	)

	class Meta:
		model = Rating
		fields = ("star",)
