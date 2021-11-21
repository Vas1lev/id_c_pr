from base.models import Info, Department, Description
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response













def django_models_json(request):
    data = list(Info.objects.values())
    # data = list(Description.objects.values())
    # infos = Info.objects.filter()
    # data = InfoSerializer(infos, many=True).data
    # return HttpResponse(data)

    # for x in data:
    #     x["department"] = x.pop("department_id")




    # for x in data:
    #     x["department_id"] = list(Info.objects.values('department'))
    # [x.pop("department_id") for x in data]
    # data + list(Info.objects.values('department'))
    # data1 = list(Info.objects.values("department__name"))
    # data_2 = [*data, *data1]

    # for dep in data:
    #     dep["department"] = list(Info.objects.values('department__name'))

    # val = []
    # for x in data:
    #     for y in x.get("department"):
    #         for value in y.values():
    #             val.append(value)
    # [x.pop("department") for x in data]
    # for t in data:
    #     t["department"] = val





    return JsonResponse(data, safe=False)

