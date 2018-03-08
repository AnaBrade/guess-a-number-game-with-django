from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from random import randint


secret_number = randint(0, 100)
turn = 0
success = False

# Create your views here.
@csrf_exempt
def guess_game(request):
    global secret_number, turn, success
    context = {}
    hint = ''
    guessed_number = None

    if request.method == 'POST' and request.POST.get('guess_number'):
        guessed_number = int(request.POST['guess_number'])
        turn +=1
        if guessed_number == secret_number:
            success = True
        else:
            if(guessed_number > secret_number):
                hint = 'lower'
            else:
                hint = 'higher'
        
    else:
        secret_number = randint(0,100)
        turn = 0
        success = False
        hint = ''
        guessed_number = None
    
    context['success'] = success
    context['turn'] = turn
    context['hint'] = hint
    context['guessed_number'] = guessed_number

    return render(request, 'guess_game_index.html', context)