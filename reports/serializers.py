from reports.models import Report
from rest_framework import serializers


# Serializers define the API representation.
class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ('title', 'content', 'author', 'applicant', 'is_public',)
        read_only_fields = ('updated', 'created_at',)
