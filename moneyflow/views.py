from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Account


@login_required
def frontpage(request):
    context = {
        "accounts": Account.objects.filter(owner=request.user),
    }
    return render(request, "moneyflow/index.html", context)
