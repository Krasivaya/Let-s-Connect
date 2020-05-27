from django.test import TestCase
from .models import Author, Post, Comment

# Author tests
class AuthorTestClass(TestCase):

    # Setup method
    def setUp(self):
        self.carine = Author(first_name='Carine', last_name='SEMWAGA', email='carine@connect.com')

    # Test instance method
    def test_instance(self):
        self.assertTrue(isinstance(self.carine, Author))

    # Test save method
    def test_save(self):
        self.carine.save()

    # Test update method
    def test_update(self):
        Author.objects.filter(id=1).update(first_name='Admin')

    # Delete method
    def tearDown(self):
        Author.objects.all().delete()
        

# Post Tests
class PostTestClass(TestCase):

    # Setup method
    def setUp(self):
        self.carine = Author(first_name='Carine', last_name='SEMWAGA', email='carine@connect.com')
        self.carine.save()

        self.new_post = Post(
            title='Test', 
            post='This is a testing post',
            author=self.carine
        )
        self.new_post.save()

    # Test instance method
    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))

    # Test save method
    def test_save(self):
        self.new_post.save()

    # Test update method
    def test_update(self):
        Post.objects.filter(id=1).update(title='Updated Test')

    # Delete method
    def TearDown(self):
        Post.objects.all().delete()

# Comment Tests
class CommentTestClass(TestCase):

    # Setup method
    def setUp(self):
        self.carine = Author(first_name='Carine', last_name='SEMWAGA', email='carine@connect.com')
        self.carine.save()

