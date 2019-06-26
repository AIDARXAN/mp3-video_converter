from __future__ import unicode_literals
import youtube_dl

from .forms import DownloadForm
from .models import AudioFile
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
# Create your views here.


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')



def index(request):
    form = DownloadForm()
    if request.method == 'POST':
        form = DownloadForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            AudioFile.objects.create()
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'logger': MyLogger(),
                'progress_hooks': [my_hook],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                meta = ydl.extract_info(url, download=False)
                
                audio_file = AudioFile.objects.create(url=url, video_title=meta["title"])
                audio_file.save()
                
                return redirect(meta['url'])
    return render(request, "mp3_converter/index.html", context={'form': form})