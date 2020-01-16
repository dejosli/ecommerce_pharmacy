# make sure this is at the top if it isn't already
from django import forms

# our new form


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'Your Email',
               'class': 'form-control'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Your Subject',
               'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Write your message here...',
               'class': 'form-control'}), required=True)
    # the new bit we're adding

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['from_email'].label = "Email:"
        self.fields['subject'].label = "Subject:"
        self.fields['message'].label = "Message:"

