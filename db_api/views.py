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
'''
1: domaintestlog
2: domainlistall

'''

type_ = [[DomainTestLog, DomainTestLogSerializer],
         [DomainListAll, DomainListAllSerializer]]


@api_view(['POST'])
def C_data(request, tablename="domaintestlog"):
    ''' add new data to database.'''
    model, serializers = main(tablename)
    if request.method == 'POST':
        data = JSONParser().parse(request)  
        input_ = data['data']
        if tablename == "domaintestlog":
            data_serializer = serializers(data=input_, many=True)  
            if data_serializer.is_valid():  
                data_serializer.save()
                return JsonResponse(data, safe=False, status=status.HTTP_201_CREATED)
            return JsonResponse(data_serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        elif tablename == "domainlistall":
            data_serializer = serializers(data=input_, many=True)
            if data_serializer.is_valid():
                data_serializer.save()
                return JsonResponse(data, safe=False, status=status.HTTP_201_CREATED)
            return JsonResponse(data_serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({"message": "Database doesn't exists."})


@api_view(['GET'])
def R_data(request, tablename="domaintestlog"):
    '''show all of the data'''
    model, serializers = main(tablename)
    if request.method == 'GET':
        if tablename == "domaintestlog":
            domaintestlog = model.objects.all()
            if domaintestlog.count() == 0:
                return JsonResponse({'message': 'No data inside database.'})
            data_serializer = serializers(domaintestlog, many=True)
            results = {"results": data_serializer.data}
            return JsonResponse(results, safe=False)
        elif tablename == "domainlistall":
            domainlistall = model.objects.all()
            if domainlistall.count() == 0:
                return JsonResponse({'message': 'No data inside database.'})
            data_serializer = serializers(domainlistall, many=True)
            results = {"results": data_serializer.data}
            return JsonResponse(results, safe=False)
        else:
            return JsonResponse({"message": "Database doesn't exists."})


@api_view(['PUT'])
def U_data(request, id_, tablename):
    ''' update specific data using id. '''
    model, serializers = main(tablename)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        if tablename == "domaintestlog":
            domaintestlog = model.objects.get(id=id_)
            # print(domaintestlog.CDN)
            # domaintestlog.TestTime = data["TestTime"]
            # domaintestlog.save()
            data_serializer = serializers(domaintestlog, data=data)
            if data_serializer.is_valid():
                data_serializer.save()
                successed = {"successed": data_serializer.data}
                return JsonResponse(successed, status=status.HTTP_200_OK)
            return JsonResponse(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif tablename == "domainlistall":
            domainlistall = model.objects.get(id=id_)
            data_serializer = serializers(domainlistall, data=data)
            if data_serializer.is_valid():
                data_serializer.save()
                successed = {"successed": data_serializer.data}
                return JsonResponse(successed, status=status.HTTP_200_OK)
            return JsonResponse(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({"message": "Database doesn't exists."})


@api_view(['DELETE'])
def D_data(request, id_, tablename):
    ''' delete specific data using id. '''
    model, serializers = main(tablename)
    if request.method == 'DELETE':
        if tablename == "domaintestlog":
            try:
                domaintestlog = model.objects.get(id=id_)
                domaintestlog.delete()
                return JsonResponse({"message": f"ID {id_} was deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
            except:
                return JsonResponse({"message": "ID doesn't exist"}, status=status.HTTP_204_NO_CONTENT)
        elif tablename == "domainlistall":
            try:
                domainlistall = model.objects.get(id=id_)
                domainlistall.delete()
                return JsonResponse({'message': f'ID: {id_} was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
            except:
                return JsonResponse({"message": "ID doesn't exist"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({"message": "Database doesn't exists."})


@api_view(['DELETE'])
def D_all_data(request, tablename):
    ''' delete all. '''
    model, serializers = main(tablename)
    if request.method == 'DELETE':
        if tablename == "domaintestlog":
            count = model.objects.all().delete()
            print(count)
            if count[1]["myapp.DomainTestLog"] == 0:
                return JsonResponse({'message': 'Database was already empty.'})
            return JsonResponse({'message': f'Total {count[0]} was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        elif tablename == "domainlistall":
            count = model.objects.all().delete()
            print(count)
            if count[1]["myapp.DomainListAll"] == 0:
                return JsonResponse({'message': 'Database was already empty.'})
            return JsonResponse({'message': f'Total {count[0]} was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({"message": "Database doesn't exists."})


def main(tablename):
    if tablename == "domaintestlog":
        model = type_[0][0]
        serializers = type_[0][1]
    elif tablename == "domainlistall":
        model = type_[1][0]
        serializers = type_[1][1]
    else:
        tablename = None
        serializers = None
    return model, serializers