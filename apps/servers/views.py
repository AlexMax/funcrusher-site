from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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

@login_required
def password_request(request, server_id=None):
    s = None

    # Check to see if the server id exists
    try:
        s = Server.objects.get(id=server_id)
    except Server.DoesNotExist:
        return HttpResponse(status=400)

    # Check to see if the combination of server id and user exists
    try:
        PasswordPermission.objects.get(server=server_id, user=request.user.id)
    except PasswordPermission.DoesNotExist:
        # Add the combination
        pp = PasswordPermission(server=s, user=request.user)
        pp.save()

    if request.is_ajax():
        return HttpResponse(status=200)

    return render_to_response('servers/password_request.html',
            {'server': s},
            context_instance=RequestContext(request))
