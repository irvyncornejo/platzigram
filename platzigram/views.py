# platzigram views
# django
from django.http import HttpResponse

#utilities
from datetime import datetime
import json


def hello_word(request):
    # now = datetime.now().strftime('%b %d, %Y - %H hrs')
    return HttpResponse('oh, hi! Current server time is {now}'.format(
        now = datetime.now().strftime('%b %d, %Y - %H:%M hrs')))

def sort_integers(request):
    numbers = [int (i) for i in request.GET['numbers'].split(',')]
   
    sorted_ints = sorted(numbers)

    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message' : 'integers sorted successfully.'
    }
    
    return HttpResponse(
        json.dumps(data, indent = 4), content_type = 'application/json'
    )

def say_hi(request, name, age):

    if age < 12:
       message = "Sorry {}".format(name)
    else:
        message = 'welcomw {}'.format(name)

    return HttpResponse(message)