from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Job
from .serializers import JobSerializer


@api_view(['GET', 'POST'])
def job(request):
    if request.method == 'GET':
        serializer = JobSerializer(Job.objects.all(), many=True)
        return JsonResponse({'success': True, 'job': serializer.data})
    elif request.method == 'POST':
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'job': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'success': False, "messsage": serializer.errors})


@api_view(['GET', 'PUT', 'DELETE'])
def job(request, id):
    try:
        selected_job = Job.objects.filter(id=id).get()
    except Job.DoesNotExist:
        return Response({'success': False, 'errors': ["Job Not found"]}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = JobSerializer(selected_job)
        print("Method : " + request.method)
        return Response({'success': True, 'job': serialize.data}, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serialize = JobSerializer(selected_job, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({'success': True, 'job': serialize.data}, status=status.HTTP_301_MOVED_PERMANENTLY)
        else:
            return Response({'success': False, 'errors': serialize.error_messages}, status=status.HTTP_304_NOT_MODIFIED)
    elif request.method == 'DELETE':
        selected_job.delete()
        return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'success': False})


@api_view(['POST'])
def upload_image(request, id):
    try:
        selected_job = Job.objects.filter(id=id).get()
    except Job.DoesNotExist:
        return Response({'success': False, 'errors': ["Job Not found"]}, status=status.HTTP_404_NOT_FOUND)
