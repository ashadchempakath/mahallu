from django.shortcuts import redirect


def introduction(request):
    return redirect('/intro')