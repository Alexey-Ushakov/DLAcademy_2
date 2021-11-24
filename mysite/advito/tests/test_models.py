from datetime import datetime, timedelta
import os
import codecs
import tempfile

from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from advito.models import Post



class TestPostModel(TestCase):

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def setUp(self):
        dir_ = os.path.dirname(os.path.abspath(__file__))
        image = os.path.join(dir_, 'static', 'test.jpg')
        f = codecs.open(image, encoding='base64')
        self.image = SimpleUploadedFile(f.name, f.read())
        f.close()

    def test_date_edit(self):
        with self.assertRaises(ValidationError):
            my_user = User.objects.create(username='test', password='test', email='test@test.com')
            print(my_user)
            my_post = Post.objects.create(
                author=my_user,
                title='test',
                description='test',
                image=self.image,
                price=35,

            )

            print(my_post.date_edit)
            my_post.date_edit = datetime.now() + timedelta(days=1)
            print(my_post.date_edit)
            my_post.full_clean()
            my_post.save()
