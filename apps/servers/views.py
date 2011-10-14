from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Server, PasswordPermission

# Create your views here.
@login_required
def passwords(request):
    status_classes = {
        PasswordPermission.REQUEST_STATUS: 'info',
        PasswordPermission.ALLOWED_STATUS: 'success',
        PasswordPermission.DENIED_STATUS: 'danger',
    }

    servers = Server.objects.all()

    for index, server in enumerate(servers):
        try:
            status = PasswordPermission.objects.get(server=server.id,
                    user=request.user.id).status
            servers[index].status = \
                dict(PasswordPermission.STATUS_CHOICES)[status]
            servers[index].status_class = status_classes[status]
        except PasswordPermission.DoesNotExist:
            pass

    return render_to_response('servers/passwords.html',
            {'servers': servers},
            context_instance=RequestContext(request))

