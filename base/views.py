import pandas as pd
from django.shortcuts import render, get_list_or_404
from .models import Info, Department

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView

import io
import pandas


class InfoListView(ListView):
    model = Info
    template_name = 'base/main.html'






def info_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    info = get_list_or_404(Info, pk=pk)

    template_path = 'base/to_pdf.html'
    context = {'info': info}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return render('We had some errors <pre>' + html + '</pre>')
    return response


def data_frame_to_io(data_frame: pandas.DataFrame, sheet_name='Export') -> bytes:
    data_stream = io.BytesIO()
    writer = pandas.ExcelWriter(data_stream, engine='xlsxwriter')
    data_frame.to_excel(writer, index=False, sheet_name=sheet_name)
    writer.save()
    data_stream.seek(0)

    return data_stream.getvalue()


def export(request):

    data = list(Info.objects.values(
        "first_name", "last_name", "citizenship", "gen", "personal_no", "date_of_birth",
        "date_of_expiry", "signature", "card_no", "place_of_birth", "date_of_issue",
        "issuing_authority", "department__name", "image",
    ))
    for x in data:
        x["department"] = x.pop("department__name")
    results = pandas.DataFrame(data=data)
    results['date_of_issue'] = results['date_of_issue'].apply(lambda a: pd.to_datetime(a).date())
    file_data = data_frame_to_io(results)
    response = HttpResponse(file_data, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="export.xlsx"'

    return response


