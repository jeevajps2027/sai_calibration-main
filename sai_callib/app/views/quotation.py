from django.shortcuts import render


def quotation(request):
    return render(request,"app/quotation.html")