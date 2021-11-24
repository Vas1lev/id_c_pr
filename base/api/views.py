from base.models import Info, Description
from django.http import JsonResponse
# from rest_framework import viewsets
# from rest_framework.response import Response





def django_models_json(request):
    data = list(Info.objects.values(
        "first_name", "last_name", "citizenship", "gen", "personal_no", "date_of_birth",
        "date_of_expiry", "signature", "card_no", "place_of_birth", "date_of_issue",
        "issuing_authority", "department__name", "image"
    ))
    for x in data:
        x["department"] = x.pop("department__name")

    return JsonResponse(data, safe=False)

