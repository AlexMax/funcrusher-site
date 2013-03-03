from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import UserProfileForm

# Create your views here.
@login_required
def profile(request):
    flash = None
    form = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            flash = "Profile saved successfully!"
            form.save()
    else:
        form = UserProfileForm(instance=request.user.profile)

    return render_to_response('profiles/profile.html',
            {'form': form, 'flash': flash},
            context_instance=RequestContext(request))
