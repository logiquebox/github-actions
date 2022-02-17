from django.test import TestCase
from .models import Post


class ModelTesting(TestCase):

    def setUp(self):
        """use model specifications to setup database"""
        self.blog = Post.objects.create(title='django', author='django', slug='django')

    def test_post_model(self):
        """Test creating a new post model"""
        d = self.blog

        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'django')
