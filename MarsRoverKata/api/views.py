from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from api.models import Rover


@csrf_exempt
def moveRoverApi(request, id=0):
    if request.method == 'POST':
        rover = Rover.objects.get(id=id)
        data = JSONParser().parse(request)
        sequence = data['sequence']

        for c in sequence:
            if c not in ['l', 'r', 'f', 'b']:
                return JsonResponse("Wrong sequence, must only contain l, r, f, b characters", safe=False, status=400)

        if not rover.followSequence(sequence):
            return JsonResponse("Warning obstacle detected at position aborting sequence!", safe=False, status=409)
        return JsonResponse("Rover reached destination Successfully!", safe=False)