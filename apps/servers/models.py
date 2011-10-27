from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Server(models.Model):
    address = models.CharField(max_length=100, help_text="IP/Domain and port "
            "to connect to the server.")
    info = models.TextField(blank=True, help_text="Information about the "
            "server.")
    name = models.CharField(max_length=100, help_text="Name of the server.")
    password = models.CharField(blank=True, max_length=50, help_text="Password "
            "needed to connect to the server.")

    def __unicode__(self):
        return self.name

class PasswordPermission(models.Model):
    REQUEST_STATUS = 0
    ALLOWED_STATUS = 1
    DENIED_STATUS = 2
    STATUS_CHOICES = (
        (REQUEST_STATUS, 'Requested'),
        (ALLOWED_STATUS, 'Allowed'),
        (DENIED_STATUS, 'Denied'),
    )

    created = models.DateTimeField(auto_now_add=True)
    server = models.ForeignKey(Server)
    status = models.IntegerField(choices=STATUS_CHOICES,
            default=REQUEST_STATUS, help_text="Is the user allowed to see the "
            "server password?")
    user = models.ForeignKey(User)
    user_modified = models.ForeignKey(User, blank=True, null=True,
            related_name='password_permission_modified_set')

    class Meta:
        ordering = ['-created']
