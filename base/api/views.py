from base.models import Info
from django.http import JsonResponse


def django_models_json(request):
    data = list(Info.objects.values())
    return JsonResponse(data, safe=False)

