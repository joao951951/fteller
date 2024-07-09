from django.shortcuts import render
import random

fortuneList = [
    "A vida trará coisas boas se tiver paciência.",
    "Demonstre amor e alegria em todas as oportunidades e verá que a paz nasce dentro de si.",
    "Não compense na ira o que lhe falta na razão.",
    "Defeitos e virtudes são apenas dois lados da mesma moeda.",
    "A maior de todas as torres começa no solo."
]

# Create your views here.
def tune(request):
    context = { 'fortune': random.choice(fortuneList)}
    return render(request, 'randomzer/tune.html', context)