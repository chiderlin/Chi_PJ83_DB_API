from db_api.models import DomainListAll, DomainTestLog
from rest_framework import serializers

class DomainTestLogListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        data = [DomainTestLog(**item) for item in validated_data]
        return DomainTestLog.objects.bulk_create(data) 


class DomainListAllListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        data = [DomainListAll(**item) for item in validated_data]
        return DomainListAll.objects.bulk_create(data)



class DomainListAllSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = DomainListAllListSerializer
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


class DomainTestLogSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = DomainTestLogListSerializer
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