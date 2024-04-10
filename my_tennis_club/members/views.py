from django.shortcuts import render
from .models import Lignes

def index(request):
    trains = Lignes.objects.all()  # Récupérer tous les trains depuis le modèle Lignes
    return render(request, 'index.html', {'trains': trains})

def show_train(request, train_id):
    # Récupérer l'objet Lignes avec l'identifiant train_id
    lignes = Lignes.objects.get(pk=train_id)
    # Rendre le template en passant l'objet lignes
    return render(request, 'show.html', {'lignes': lignes})

