from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Tag
from .serializers import TagSerializer


# Create your views here
@api_view(['GET', 'POST'])
def tag(request):
    if request.method == 'GET':
        serializer = TagSerializer(Tag.objects.all(), many=True)
        return JsonResponse({'success': True, 'tag': serializer.data})
    else:
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'tag': serializer.data}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def tag(request, id):
    try:
        selected_tag = Tag.objects.filter(pk=id).get()
    except Tag.DoesNotExist:
        return Response({'status': False, 'errors': ["Tag Not found"]}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = TagSerializer(selected_tag)
        return Response({'success': True, 'tag': serialize.data}, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serialize = TagSerializer(selected_tag, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({'success': True, 'tag': serialize.data}, status=status.HTTP_301_MOVED_PERMANENTLY)
        else:
            return Response({'success': False, 'errors': serialize.error_messages}, status=status.HTTP_304_NOT_MODIFIED)
    elif request.method == 'DELETE':
        selected_tag.delete()
        return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)
