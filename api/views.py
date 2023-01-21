from django.shortcuts import render
from django.db.models import Prefetch
from django.db.models.query import prefetch_related_objects
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import IsAuthenticated
from .models import Document
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db import connection
from .serializers import DocumentsSerializer, RegisterSerializer, TrackSerializer
from django.conf import settings
import pytesseract    # ======= > Add
from pdf2image import convert_from_path
try:
    from PIL import Image
except:
    import Image
import openai

openai.api_key = "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"
# Create your views here.


@api_view(['GET'])
def apiOverview(request):

    path = {
        "asdfsdf": "sdfsafd",
        "asdfsafd": "asdfsadf"
    }

    return Response(path)


@api_view(['POST'])
def registerUser(request):

    userData = RegisterSerializer(data=request.data)
    data = {}
    if userData.is_valid():
        user = userData.save()
        data['success'] = "success"
    else:
        data['success'] = "failure"

    return Response(data)

@api_view(["POST"])
def updateTrack(request):
    track = TrackSerializer(data = request.data)
    data = {}
    if track.is_valid():
        user = track.save()
        data['success'] = "success"
    else:
        data['success'] = "failure"

    return Response(data) 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTracks(request):
    userId = request.user.id
    tracks = Document.objects.filter(user=userId).order_by("-id")
    allTracks = TrackSerializer(tracks, many=True)
    return Response(allTracks.data)

@api_view(["POST"])
def uploadDocuments(request):
    documents = DocumentsSerializer(data=request.data)
    data = {}
    if documents.is_valid():
        user = documents.save()
        data['success'] = "success"
    else:
        data['success'] = "failure"

    return Response(data)

@api_view(['GET'])
def getDocuments(request, pk):
    print(pk)
    docs = Document.objects.filter(user=pk, encrypted = False).order_by("-id")
    documents = DocumentsSerializer(docs, many=True)
    return Response(documents.data)

@api_view(['GET'])
def analyzeDocuments(request, pk):
    print(pk)
    docs = Document.objects.get(id=pk)
    document = DocumentsSerializer(docs, many=False)
    path = f"static{document.data['document']}"
    print(path)
    if "pdf" in document.data['document']:
        image = convert_from_path(path)
        text = pytesseract.image_to_string(image[0])
    else:
        text = pytesseract.image_to_string(Image.open(path))
    encoded_text = text.encode('ascii', 'ignore').decode('unicode_escape')
    prompt = f"{encoded_text} . What can we infer from the given medical report above ."

    # Generate text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        temperature=1,
        user="dhruv"
    )
    print(response.choices[0].text.encode(
        'ascii', 'ignore').decode('unicode_escape'))

    return Response(response.choices[0].text.encode('ascii', 'ignore').decode('unicode_escape'))

@api_view(['GET'])
def getQR(request):
    Qr.objects.create(url="https://google.com")

    return Response("Qr is created")