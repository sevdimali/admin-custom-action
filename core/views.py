from django.core import serializers
from django.http import HttpResponse
from core.models import Company


def export(request):
    ids = request.GET.get('ids').split(',')
    qs = Company.objects.filter(id__in = ids)
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", qs, stream=response)
    return response
