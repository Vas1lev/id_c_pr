from django.urls import path
from base.api import views as api_views
from .views import InfoListView, info_render_pdf_view, export

app_name = 'base'

urlpatterns = [
    path('', InfoListView.as_view(), name='info-base-view'),
    path('pdf/<pk>/', info_render_pdf_view, name='info-pdf-view'),
    path('json/', api_views.django_models_json, name='info-json-view'),
    path('excel/', export, name='excel'),
]