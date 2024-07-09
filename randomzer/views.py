from django.shortcuts import render

# Create your views here.
def tune(request):
    context = {}
    return render(request, 'randomizer/tune.html', context)