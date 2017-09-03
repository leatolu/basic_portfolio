from django.test import TestCase
from django.db import utils
from .models import Gallery, Slide, Image


class GalleryModelTests(TestCase):

    def test_title_must_be_unique(self):
        """
            Gallery naming should be unique so that
            URLs can be parsed. Creating two galleries
            with identical titles should raise an
            error.
        """
        title = 'test_title'
        Gallery.objects.create(title=title)
        passed = False
        try:
            Gallery.objects.create(title=title)
        except:
            passed = True
        assert(passed)
