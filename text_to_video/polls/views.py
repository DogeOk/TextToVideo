from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.conf import settings
from TextToVideo import TextToVideo
from PIL import ImageFont
import os
from .models import *
import datetime

def index(request):
    print(Responses.objects.values_list("responses", flat=True))
    return HttpResponse("Просто индекс")

def text_to_video(request):
    user_message = request.GET.get("message", "")
    responses_db = Responses.objects.create(responses=user_message, date=datetime.datetime.now())
    responses_db.save()
    vid_from_text = TextToVideo(user_message, (100, 100), ImageFont.truetype("StampatelloFaceto.otf", 12))
    vid_from_text.create_video(duration=3, fps=15)
    path = "video.mp4"
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/video")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
