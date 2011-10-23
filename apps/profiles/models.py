from django.contrib.auth.models import User
from django.db import models
from registration.signals import user_registered

# Create your models here.
class Profile(models.Model):
    admin_notes = models.TextField(blank=True, help_text="Notes on this user "
            "should be kept here.  This field can only be seen by admins.")
    aliases = models.TextField(blank=True, help_text="Any common alises this "
            "user has volunteered.")
    contact = models.TextField(help_text="Additional contact information this "
            "user as volunteered.")
    location = models.CharField(max_length=50, help_text="A real-life "
            "location for this user.")
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username + "'s profile"

# Signals
def user_created(sender, user, request, **kwargs):
    from forms import UserRegistrationForm

    form = UserRegistrationForm(request.POST)
    data = Profile(user=user)
    data.aliases = form.data['aliases']
    data.contact = form.data['contact']
    data.location = form.data['location']
    data.save()

user_registered.connect(user_created)
