from django.shortcuts import render
from django.http.response import JsonResponse
from django.core import serializers
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from db_api.models import DomainTestLog, DomainListAll, Files
from db_api.serializers import DomainTestLogSerializer, DomainListAllSerializer, FileSerializer
import time


# Create your views here.
@api_view(['POST'])
def C_data_DomainTestLog(request):
    ''' add new data to database.'''
    if request.method == 'POST':
        data = JSONParser().parse(request)
        results = data['results']
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
        return JsonResponse(data_serializer.data, safe=False) # 'safe=False' for objects serialization


@api_view(['PUT'])
def U_data_DomainTestLog(request, id_):
    ''' update specific data using id. '''
    if request.method == 'PUT':
        domaintestlog = DomainTestLog.objects.using('default').get(id=id_)
        data = JSONParser().parse(request)
        # print(domaintestlog.CDN)
        # domaintestlog.TestTime = data["TestTime"]
        # domaintestlog.save()
        data_serializer = DomainTestLogSerializer(domaintestlog, data =data)
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
        results = data['results']
        results_data = []
        for result in results:
            results_data.append(DomainListAll(
                AgentID = result['AgentID'],
                CodeToMatch = result['CodeToMatch'],
                DomainListAPP = result['DomainListAPP'],
                DomainListInner = result['DomainListInner'],
                DomainListOuter = result['DomainListOuter'],
            ))
        DomainListAll.objects.using('default').bulk_create(results_data)
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
        return JsonResponse(data_serializer.data, safe=False)# 'safe=False' for objects serialization


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

#FIXME:未成功
class FileView(APIView):
    parser_classes = (FileUploadParser, JSONParser, FormParser, MultiPartParser,)
    # parser_classes = (JSONParser,)
    def post(self, request, format=None):
        print(request.content_type)
        # print(request.data)
        print("111")
        # print(request.POST)
        # print(request.FILES)
        # print(request.data)
        # data = request.data['file']
        # print(data)
        print("2222")
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return JsonResponse(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        files = Files.objects.all()
        file_serializer = FileSerializer(files, many=True)
        return JsonResponse(file_serializer.data, status=status.HTTP_200_OK)



# @api_view(['POST'])
# def upload_file(request):
#     if request.method == 'POST':
#         file_ob = open(r'D:\PJ83\env01\PJ83_db_api\11.txt', "rb")
#         print(file_ob)
#         payload = {
#         'Remark1': 'hey',
#         'Remark2': 'hello',
#         'File': file_ob
#         }
#         r = requests.post("http://127.0.0.1:8080/api/7zfile/download/", files=file_ob, data=payload)
#         print(r.status_code)

#     #     with open(f,"rb") as z:
#     #         binary = z.read()
#     #         return JsonResponse({'message':f'{binary}'})
#     # else:
#     #     return JsonResponse({'message':'POST only'})
# @api_view(['GET'])
# def download_file(request):
#     pass

