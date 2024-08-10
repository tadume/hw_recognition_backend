from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def predict(request):
    if request.body:
        body = json.loads(request.body)
        print(body)

    return HttpResponse(status=200)