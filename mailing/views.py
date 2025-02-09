from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from client.models import Client
from mailing.forms import MessageForm, SendingForm, SendingManageForm
from mailing.models import Sending, Message, Status


# ListView


class SendingListView(PermissionRequiredMixin, ListView):
    model = Sending
    permission_required = 'mailing.view_sending'


class MessageListView(ListView):
    model = Message


class StatusListView(ListView):
    model = Status


# DetailView


class SendingDetailView(LoginRequiredMixin, DetailView):
    model = Sending
    login_url = "users:login"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        clients_detail = Client.objects.all()
        context_data['clients_all'] = clients_detail
        return context_data


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    login_url = "users:login"


# CreateView


class SendingCreateView(LoginRequiredMixin, CreateView):
    model = Sending
    form_class = SendingForm
    success_url = reverse_lazy("mailing:sending_list")
    login_url = "users:login"

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.creator = self.request.user
            self.object.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")
    login_url = "users:login"

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.creator = self.request.user
            self.object.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


# UpdateView


class SendingUpdateView(LoginRequiredMixin, UpdateView):
    model = Sending
    form_class = SendingForm
    success_url = reverse_lazy("mailing:sending_list")
    login_url = "users:login"

    def get_form_class(self):
        user = self.request.user
        if user == self.object.creator or user.is_superuser:
            return SendingForm
        if user.has_perm('catalog.can_edit_status'):
            return SendingManageForm
        raise PermissionDenied


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")
    login_url = "users:login"


# DeleteView


class SendingDeleteView(LoginRequiredMixin, DeleteView):
    model = Sending
    success_url = reverse_lazy("mailing:sending_list")
    login_url = "users:login"


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy("mailing:message_list")
    login_url = "users:login"




