from django.forms import ModelForm, Form, IntegerField
from dal import autocomplete


from userfollows.models import Userfollow


class UserfollowForm(ModelForm):
    class Meta:
        model = Userfollow
        fields = ('followed_user',)
        labels = {"followed_user": "nom d'utilisateur"}
        widgets = {
            'followed_user': autocomplete.ModelSelect2(url='user-autocomplete')
        }


class UnfollowForm(Form):
    followed_user = IntegerField()
