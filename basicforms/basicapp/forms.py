from django import forms
from django.core import validators

# def check_for_z(value): #value keywork for djangoproject
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name needs to start with Z")

class FormName(forms.Form):
    #name = forms.CharField(validators=[check_for_z])
    name = forms.CharField(label='Full Name')
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(label='Comments',widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']
        if email != verify_email:
            raise forms.ValidationError("Please make sure the emails match")

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Gotcha bot!")
    #     return botcatcher
