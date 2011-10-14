from django import forms
from registration.forms import RegistrationForm

class UserRegistrationForm(RegistrationForm):
    location = forms.CharField(help_text="A real-life location.  A US state "
            "or non-US country is specific enough.", max_length=50)
    contact = forms.CharField(help_text="Contact information above and beyond "
            "your e-mail address, an IRC channel for example.",
            widget=forms.Textarea)
    aliases = forms.CharField(help_text="Any common aliases you tend to use "
            "on a server.", required=False, widget=forms.Textarea)
