from django import forms

from profiles.models import Profile, Publication



class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        
class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['authors', 'journal_name', 'level', 'publisher', 'date_published', 'file_upload']
        widgets = {
            'date_published': forms.DateInput(attrs={'type': 'date'}),
        }


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg


