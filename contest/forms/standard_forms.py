from django import forms


class AuthorForm(forms.Form):
    first_name = forms.CharField(label="First name", required=False)
    last_name = forms.CharField(label="Last name", required=False)
    band_name = forms.CharField(label="Band name")
    birth_date = forms.DateField(
        label="Birth date",
        required=False,
        input_formats=['%d/%m/%Y']
    )
    debut = forms.DateField(
        label="Debut date",
        required=False,
        input_formats=['%d/%m/%Y']
    )


class LoginForm(forms.Form):
    username = forms.CharField(label="Login", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class VoteForm(forms.Form):
    song_data = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'song-data'}))


class ContestSubmissionForm(forms.Form):
    song_data = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'song-data'}))
    first_name = forms.CharField(label='Imię')
    last_name = forms.CharField(label='Nazwisko')
    telephone = forms.CharField(label='Telefon')
    email = forms.CharField(label='Email', widget=forms.EmailInput)
    context = forms.CharField(label='Twoja odpowiedź', widget=forms.Textarea)