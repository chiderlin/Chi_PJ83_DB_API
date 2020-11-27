from django.shortcuts import render
from django.http.response import JsonResponse
from django.core import serializers
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework import status
from rest_framework.decorators import api_view
from db_api.models import DomainTestLog, DomainListAll
from db_api.serializers import DomainTestLogSerializer, DomainListAllSerializer
import time

# Create your views here.
@api_view(['POST'])
def C_data_DomainTestLog(request):
    ''' add new data to database.'''
    if request.method == 'POST':
        data = JSONParser().parse(request)
        # data_serializer = DomainTestLogSerializer(data=data, many=True,)
        # if data_serializer.is_valid():
        #     data_serializer.save()
        #     return JsonResponse(data_serializer.data, safe=False, status=status.HTTP_201_CREATED)
        # return JsonResponse(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        results = data['data']
        results_data = []
        for result in results:
            results_data.append(DomainTestLog(
                TestTime = result['TestTime'],
                UrlIn = result['UrlIn'],
                UrlOut = result['UrlOut'],
                MyIP = result['MyIP'],
                MyZone = result['MyZone'],
                CDN = result['CDN'],
                CDNIP = result['CDNIP'],
                PageLoadTime = result['PageLoadTime'],
                Status = result['Status'],
                IPScreenshot = result['IPScreenshot'],
                ProductScreenshot1 = result['ProductScreenshot1'],
                ProductScreenshot2 = result['ProductScreenshot2'],
                ProductScreenshot3 = result['ProductScreenshot3'],
                ProductScreenshot4 = result['ProductScreenshot4'],
            ))
        DomainTestLog.objects.using('default').bulk_create(results_data)
        return JsonResponse(data, status=status.HTTP_201_CREATED)
    return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def R_data_DomainTestLog(request):
    '''show all of the data'''
    if request.method == 'GET':
        domaintestlog = DomainTestLog.objects.using('slave').all()
        if domaintestlog.count() == 0:
            return JsonResponse({'message':'No data inside database.'})
        data_serializer = DomainTestLogSerializer(domaintestlog, many=True)
        results = {'results':data_serializer.data}
        return JsonResponse(results, safe=False) # 'safe=False' for objects serialization


@api_view(['PUT'])
def U_data_DomainTestLog(request, id_):
    ''' update specific data using id. '''
    if request.method == 'PUT':
        domaintestlog = DomainTestLog.objects.using('default').get(id=id_)
        data = JSONParser().parse(request)
        # print(domaintestlog.CDN)
        # domaintestlog.TestTime = data["TestTime"]
        # domaintestlog.save()
        data_serializer = DomainTestLogSerializer(domaintestlog, data=data)
        if data_serializer.is_valid():
            data_serializer.save()
            return JsonResponse(data_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def D_data_DomainTestLog(request,id_):
    ''' delete specific data using id. '''
    if request.method == 'DELETE':
        domaintestlog = DomainTestLog.objects.using('default').get(id=id_)
        domaintestlog.delete() 
        return JsonResponse({'message': f'ID {id_} was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def D_all_data_DomainTestLog(request):
    ''' delete all. ''' 
    if request.method == 'DELETE':
        count = DomainTestLog.objects.using('default').all().delete()
        # print(count)
        if count[1]["db_api.DomainTestLog"] == 0:
            return JsonResponse({'message':'Database was already empty.'})
        return JsonResponse({'message': f'Total {count[0]} was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

#==========================================================

@api_view(['POST'])
def C_data_DomainListAll(request):
    ''' add new data to database.'''
    if request.method == 'POST':
        data = JSONParser().parse(request)
        results = data['data']
        results_data = []
        for result in results:
            results_data.append(DomainListAll(
                AgentID = result['AgentID'],
                CodeToMatch = result['CodeToMatch'],
                DomainListAPP = result['DomainListAPP'],
                DomainListInner = result['DomainListInner'],
                DomainListOuter = result['DomainListOuter'],
            ))
        test = DomainListAll.objects.using('default').bulk_create(results_data)
        print(test)
        return JsonResponse(data, status=status.HTTP_201_CREATED)
    return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def R_data_DomainListAll(request):
    '''show all of the data.'''
    if request.method == 'GET':
        domainlistall = DomainListAll.objects.using('slave').all()
        if domainlistall.count() == 0:
            return JsonResponse({'message':'No data inside database.'})
        data_serializer = DomainListAllSerializer(domainlistall, many=True)
        results = {'results':data_serializer.data}
        return JsonResponse(results, safe=False)# 'safe=False' for objects serialization


@api_view(['PUT'])
def U_data_DomainListAll(request, id_):
    ''' update specific data using id. '''
    if request.method == 'PUT':
        domainlistall = DomainListAll.objects.using('default').get(id=id_)
        data = JSONParser().parse(request)
        data_serializer = DomainListAllSerializer(domainlistall, data=data)
        if data_serializer.is_valid():
            data_serializer.save()
            return JsonResponse(data_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def D_data_DomainListAll(request, id_):
    ''' delete specific data using id. '''
    if request.method == 'DELETE':
        domainlistall = DomainListAll.objects.using('default').get(id=id_)
        domainlistall.delete() 
        return JsonResponse({'message': f'ID {id_} was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def D_all_data_DomainListAll(request):
    ''' delete all. ''' 
    if request.method == 'DELETE':
        count = DomainListAll.objects.using('default').all().delete()
        # print(count)
        if count[1]["db_api.DomainListAll"] == 0:
            return JsonResponse({'message':'Database was already empty.'})
        return JsonResponse({'message': f'Total {count[0]} was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
