from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from api.tensorflow import image_preprocessing
@csrf_exempt
def predict(request):
    body = json.loads(request.body)
    base64image = body["image"].split(",")[1]
    numpy_image = image_preprocessing.base64_to_numpy(base64image)

    return HttpResponse(status=200)