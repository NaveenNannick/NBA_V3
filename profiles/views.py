from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from profiles.forms import ProfileForm, PublicationForm, form_validation_error
from profiles.models import Profile, Publication


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


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import Publication
from .forms import PublicationForm


@method_decorator(login_required, name='dispatch')
class PublicationListView(ListView):
    model = Publication
    template_name = 'publication_list.html'
    context_object_name = 'publications'


@method_decorator(login_required, name='dispatch')
class PublicationCreateView(CreateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'publication_form.html'
    success_url = reverse_lazy('publication_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PublicationUpdateView(UpdateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'publication_form.html'
    success_url = reverse_lazy('publication_list')


@method_decorator(login_required, name='dispatch')
class PublicationDeleteView(DeleteView):
    model = Publication
    template_name = 'publication_confirm_delete.html'
    success_url = reverse_lazy('publication_list')


@login_required
def publication_detail(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    return render(request, 'publication_detail.html', {'publication': publication})
