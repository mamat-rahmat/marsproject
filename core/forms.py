from django import forms
from django_summernote.widgets import SummernoteWidget
from registration.forms import RegistrationFormUniqueEmail
from .models import Answer, UserProfile, Topic, Post, ROLE_CHOICES, BIDANG_CHOICES


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [f"no{i:02}" for i in range(1,51)]


class UserProfileRegistrationForm(RegistrationFormUniqueEmail):
    nama_lengkap = forms.CharField(required=True)
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)
    nomor_whatsapp = forms.CharField(required=True)
    sekolah = forms.CharField(required=True)
    kota = forms.CharField(required=True)
    provinsi = forms.CharField(required=True)
    bidang = forms.ChoiceField(choices=BIDANG_CHOICES, required=True)
    guru_pembimbing = forms.CharField()
    nomor_guru_pembimbing = forms.CharField()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': SummernoteWidget(),
        }