from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from os import path

# Create your models here.
class Server(models.Model):
    address = models.CharField(max_length=100, help_text="IP/Domain and port "
            "to connect to the server.")
    config_file = models.CharField(max_length=50, help_text="Name of the "
            "configuration file where the server password will be written to. "
            "This setting should only be touched by AlexMax; if you change "
            "this yourself it might cause the server to no longer update the "
            "password.")
    info = models.TextField(blank=True, help_text="Information about the "
            "server.")
    name = models.CharField(max_length=100, help_text="Name of the server.")
    password = models.CharField(blank=True, max_length=50, help_text="Password "
            "needed to connect to the server.  Any server that shares the "
            "same configuration file will also update to the new password. "
            "The server must be restarted for the new password to take "
            "effect (just quit the server, it will restart by itself).")

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Make sure the config file is just a file and doesn't try to
        # traverse any directories.
        self.config_file = path.basename(self.config_file)
        super(Server, self).save(*args, **kwargs)

def zdoom_escape(string):
    """Escape a string so it can be used in a ZDoom string literal."""
    string = string.replace('\\', '\\\\')
    string = string.replace('\"', '\\\"')
    return string

# Signals
def update_passwords(sender, instance, created, raw, using, **kwargs):
    # Write the password file.
    fh = open(settings.SITE_ROOT + 'var/cfg/' + instance.config_file, 'w+')
    fh.write('sv_password "{password}"\nsv_joinpassword "{password}"\n'.format(
        password=zdoom_escape(instance.password)
    ))
    fh.close()

    # If two servers are sharing the same password file, they must use the
    # same password.
    post_save.disconnect(update_passwords, sender=Server)
    servers = sender.objects.filter(config_file=instance.config_file)
    for server in servers:
        server.password = instance.password
        server.save()
    post_save.connect(update_passwords, sender=Server)

post_save.connect(update_passwords, sender=Server)

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

    def __unicode__(self):
        return '{0} in {1} Permission'.format(self.user, self.server)
