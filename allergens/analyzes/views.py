from django.shortcuts import render

def analyzes(request):
    return render(request, 'analyzes/dashboard.html')
