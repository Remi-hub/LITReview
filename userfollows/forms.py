from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import ModelForm
from dal import autocomplete


from userfollows.models import Userfollow




class UserfollowForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['followed_user'].queryset = User.objects.exclude(following=True) # not follow yet


    # changer les fields de followed_user,
    # ne pas afficher les gens deja followed



    class Meta:
        model = Userfollow
        fields = ('followed_user',)
        labels = {"followed_user": "nom d'utilisateur"}
        widgets = {
            'followed_user': autocomplete.ModelSelect2(url='user-autocomplete')
        }




