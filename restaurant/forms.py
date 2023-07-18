from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from restaurant.models import Cook, Dish, DishType


class CookForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "years_of_experience"
        )


class UpdateExperienceForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = (
            "years_of_experience",
        )

    def clean_years_of_experience(self):
        years = self.cleaned_data["years_of_experience"]
        if years < 0 or years > 90:
            raise forms.ValidationError("Years of experience must be positive")
        return years


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=Cook.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Dish
        fields = (
            "__all__"
        )


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = (
            "__all__"
        )
