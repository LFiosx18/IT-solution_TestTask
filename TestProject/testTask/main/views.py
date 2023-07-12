from wsgiref.util import FileWrapper

from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from .forms import SettingsFrom
from .create_video import create_video
from .models import Settings


def index(requests):
    if requests.method == 'POST':
        form = SettingsFrom(requests.POST)
        if form.is_valid():
            form.save()
            setting = Settings.objects.last()
            if create_video(setting.title, setting.color_text, setting.color_back, setting.fps, setting.time,
                            setting.width, setting.height):
                file = FileWrapper(open('main/media/result.mp4', 'rb'))

                response = HttpResponse(file, content_type='video/mp4')
                response['Content-Disposition'] = 'attachment; filename=my_video.mp4'

                return response

    form = SettingsFrom()
    context = {
        'form': form
    }
    return render(requests, 'main/index.html', context)
