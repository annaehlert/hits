from django import forms


class AuthorForm(forms.Form):
    first_name = forms.CharField(label="First name", required=False)
    last_name = forms.CharField(label="Last name", required=False)
    birth_date = forms.DateField(label="Birth date", required=False)
    band_name = forms.CharField(label="Band name")
    debut = forms.DateField(label="Debut date", required=False)
