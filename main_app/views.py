from django.shortcuts import render
from users.models import Owners
from django.db import connection
from accounts.models import Account


def homepage_view(request):
    # curse = connection.cursor()
    # accounts = curse.execute('select * from accounts_account')
    accounts = Account.objects.raw("select * from accounts_account")
    context = {
        "accounts": accounts,
    }
    return render(request, 'home.html', context)
