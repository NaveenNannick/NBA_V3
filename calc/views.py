from django.shortcuts import render
from django.template import loader
from profiles.models import Profile
# Create your views here.
def dashboard(request):
    query_set = Profile.objects.all()
    for profile in query_set:
        print(profile)
    return render(request,"dashboard.html", { 'profiles':list(query_set)})