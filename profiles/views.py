from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from profiles.forms import ProfileForm, form_validation_error
from profiles.models import Profile


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'profile': self.profile, 'segment': 'profile'}
        return render(request, 'profiles/profile.html', context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            profile = form.save()
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.email = form.cleaned_data.get('email')
            profile.user.save()
            
            profile.birthday = form.cleaned_data['birthday']
            profile.gender = form.cleaned_data['gender']
            profile.phone = form.cleaned_data['phone']
           
            profile.institution = form.cleaned_data['institution']
            profile.department = form.cleaned_data['department']
            profile.yearofjoining = form.cleaned_data['yearofjoining']
            profile.phd = form.cleaned_data['phd']
            profile.designation = form.cleaned_data['designation']
            profile.qualifications = form.cleaned_data['qualifications']
           
            profile.oneweek = form.cleaned_data['oneweek']
            profile.program_name01 = form.cleaned_data['program_name01']
            profile.start_date01 = form.cleaned_data['start_date01']
            profile.end_date01 = form.cleaned_data['end_date01']
            profile.twoweek = form.cleaned_data['twoweek']
            profile.program_name02 = form.cleaned_data['program_name02']
            profile.start_date02 = form.cleaned_data['start_date02']
            profile.end_date02 = form.cleaned_data['end_date02']
            
            profile.interaction = form.cleaned_data['interaction']
            profile.iidate = form.cleaned_data['iidate']
            profile.iiname = form.cleaned_data['iiname']

            profile.save()

            messages.success(request, 'Profile saved successfully')
        else:
            messages.error(request, form_validation_error(form))
        return redirect('profile')
