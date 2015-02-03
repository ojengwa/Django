from django.shortcuts import render
from reports.models import Report
from reports.serializers import ReportSerializer
from rest_framework import viewsets

# Create your views here.
class ReportViewSet(viewsets.ModelViewSet):
	queryset = Report.objects.all()
	serializer_class = ReportSerializer
