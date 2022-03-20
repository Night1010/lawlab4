from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ImageSerializer, AdventureSerializer
from .models import Image, Adventurer
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Create': '/adventurer/',
        'Read': '/adventurer/<int:pk>',
        'Update': '/adventurer/<int:pk>/',
        'Delete': '/adventurer/<int:pk>/',
        'Upload Image': '/img/'
    }

    return Response(api_urls)


@require_http_methods(["GET"])
@api_view(['GET'])
def detail_adventurer(request, pk):
    adventurer = get_object_or_404(Adventurer, pk=pk)
    serializer = AdventureSerializer(adventurer, many=False)
    return Response(serializer.data,
                    status=status.HTTP_200_OK)


@require_http_methods(["POST"])
@api_view(['POST'])
def create_adventurer(request, *args, **kwargs):
    adventurer = AdventureSerializer(data=request.data)
    if adventurer.is_valid():
        adventurer.save()

    return Response(adventurer.data, status=status.HTTP_200_OK)


@require_http_methods(["PUT"])
@api_view(['PUT'])
def update_adventurer(request, pk):
    adventurer = get_object_or_404(Adventurer,pk=pk)
    serializer = AdventureSerializer(instance=adventurer, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@require_http_methods(["DELETE"])
@api_view(['DELETE'])
def delete_adventurer(request, pk):
    adventurer = get_object_or_404(Adventurer,pk=pk)
    adventurer.delete()

    return Response('Mahasiswa berhasil di delete!')


@api_view(['POST'])
def upload_image(request):
    print(request.data)
    image_file = ImageSerializer(data=request.data)
    if image_file.is_valid():
        image_file.save()

    return Response(image_file.data)
