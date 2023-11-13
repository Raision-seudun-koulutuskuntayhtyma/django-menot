from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from .models import Account, Document


@login_required
def frontpage(request):
    return render(request, "moneyflow/index.html")


class AccountView(View):
    model = Account

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class AccountsList(LoginRequiredMixin, AccountView, ListView):
    pass


class AccountDetail(LoginRequiredMixin, AccountView, DetailView):
    pass


@login_required
def documents(request):
    context = {
        "documents": Document.objects.filter(owner=request.user),
    }
    return render(request, "moneyflow/documents.html", context)
