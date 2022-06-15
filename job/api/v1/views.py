from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, UpdateAPIView, ListCreateAPIView
from job.api.v1.serializers import JobSerializer, JobCreateSerializer
from job.models import Job

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def job_list(request):
    job_objects = Job.objects.all()
    serializer = JobSerializer(job_objects, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def job_details(request, job_id):
    job_object = Job.objects.get(pk=job_id)
    serializer = JobSerializer(job_object)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def job_create(request):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    serializer = JobCreateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        response['status'] = status.HTTP_201_CREATED

    else:
        response['data'] = serializer.errors
        response['status'] = status.HTTP_400_BAD_REQUEST

    return Response(**response)


@api_view(['PUT', 'PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def job_update(request, job_id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    job_instance = Job.objects.get(pk=job_id)
    if request.method == 'PUT':
        serializer = JobSerializer(
            instance=job_instance, data=request.data)
    else:
        serializer = JobSerializer(
            instance=job_instance, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        response['status'] = status.HTTP_201_CREATED

    else:
        response['data'] = serializer.errors
        response['status'] = status.HTTP_400_BAD_REQUEST

    return Response(**response)


@api_view(['DELETE'])
def job_delete(request, job_id):
    Job.objects.get(pk=job_id).delete()
    return Response(data={'details': 'Job deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
