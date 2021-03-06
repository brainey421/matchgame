from django.shortcuts import render

def index(request):
    return render(request, 'game/index.html')

def lobby(request):
    party_id = request.POST['inputPartyID']
    name = request.POST['inputName']
    context = {
        'party_id': party_id,
        'name': name
    }
    return render(request, 'game/lobby.html', context)
