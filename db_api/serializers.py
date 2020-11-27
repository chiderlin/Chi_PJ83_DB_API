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
            'DomainType',
        )

# class BulkListSerializer(serializers.ListSerializer):
#     def create(self, results):
#         data = [DomainTestLog(**result) for result in results]
#         return DomainTestLog.objects.using('default').bulk_create(data)


class DomainTestLogSerializer(serializers.ModelSerializer):
    class Meta:
        # list_serializer_class = BulkListSerializer
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
            'DomainType',
        )


