from django import forms
from django.contrib.auth import authenticate, login
from .models import default_profile_photo, User, Photo

class RequestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RequestForm, self).__init__(*args, **kwargs)

class VerifyCredentialsForm(forms.Form):
    email = forms.EmailField(required=True, min_length=4, max_length=128)
    password = forms.CharField(required=True, min_length=4, max_length=128, error_messages={
        "min_length": "The password is not strong enough."
    })

    def clean_email(self):
        email = self.data['email'].lower()

        account_exists = User.objects.filter(email=email).exists()
        if account_exists:
            # account already exists for this email, so return a conflicted response
            raise forms.ValidationError(f"User already exists with the email {email}.")
            
        return email

class SignUpForm(RequestForm, VerifyCredentialsForm):
    name = forms.CharField(max_length=128)
    location = forms.CharField(required=True, max_length=128, error_messages={
        "required": "Please input a location."
    })
    interests = forms.JSONField(required=True, error_messages={
        "required": "Please input enough interests."
    })
    biography = forms.CharField(required=True, max_length=512, error_messages={
        "required": "Please input a biography."
    })
    latitude = forms.DecimalField(required=True, max_digits=16, decimal_places=12)
    longitude = forms.DecimalField(required=True, max_digits=16, decimal_places=12)

    def save(self):
        """
        Creates a user with the provided form information.
        """

        user = User.objects.create_user(email=self.cleaned_data['email'], password=self.cleaned_data['password'])
        user.name = self.cleaned_data['name']
        user.location = self.cleaned_data['location']
        user.latitude = self.cleaned_data['latitude']
        user.longitude = self.cleaned_data['longitude']
        user.interests = self.cleaned_data['interests']
        user.biography = self.cleaned_data["biography"]
        user.profile_photo = default_profile_photo
        user.save()
        login(self.request, user)
        return user

class LoginForm(RequestForm, forms.Form):
    email = forms.EmailField(required=True, min_length=4, max_length=128)
    password = forms.CharField(required=True, min_length=4, max_length=128, error_messages={
        "min_length": "The password is not strong enough."
    })

    def clean(self):
        email = self.data['email'].lower()
        password = self.data['password']

        user = authenticate(self.request, email=email, password=password)
        if user is None:
            # the authentication failed because the email and password combination was not found
            raise forms.ValidationError(f"The email and password credentials were not found.")

        self.user = user
        return user

    def save(self):
        """
        Starts the user's session.
        """

        login(self.request, self.user)
        return self.user

class PhotoForm(forms.Form):
    photo = forms.ImageField(required=True, error_messages={
        "required": "Please upload a photo."
    })

class InterestForm(forms.Form):
    interest = forms.CharField(required=True, max_length=256, error_messages={
        "required": "Please enter an interest."
    })
    
class ChatRoomForm(forms.Form):
    profile_id = forms.IntegerField(required=True, error_messages={
        "required": "Please enter a profile id."
    })

