from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Gallery, Slide


class IndexView(generic.ListView):
    template_name = 'image_viewer/index.html'
    context_object_name = 'gallery_list'
    queryset = Gallery.objects.all()


def gallery(request, gallery_title):
    gallery = get_object_or_404(Gallery, title=gallery_title)
    slides = Slide.objects.filter(gallery=gallery.id)
    context = {
        'gallery_title': gallery.title,
        'slides': slides,
    }
    return render(request, 'image_viewer/gallery.html', context)
