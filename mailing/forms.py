from django import forms
from mailing.models import Sending, Message


class SendingForm(forms.ModelForm):

    class Meta:
        model = Sending
        fields = ('title', 'periodicity', 'message', 'clients')


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('tem_message', 'message_body')
