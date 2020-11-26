from db_api.models import DomainListAll, DomainTestLog
from rest_framework import serializers

class DomainListAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainListAll
        fields = (
            'AgentID',
            'CodeToMatch',
            'DomainListAPP',
            'DomainListInner',
            'DomainListOuter',
            'CreatedTime',
        )


class DomainTestLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainTestLog
        fields = (
            'id',
            'TestTime',
            'UrlIn',
            'UrlOut',
            'MyIP',
            'MyZone',
            'CDN',
            'CDNIP',
            'PageLoadTime',
            'Status',
            'IPScreenshot',
            'ProductScreenshot1',
            'ProductScreenshot2',
            'ProductScreenshot3',
            'ProductScreenshot4',
            'CreatedTime',
        )


