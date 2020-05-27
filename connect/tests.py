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
        # Author instance
        self.carine = Author(
            first_name='Carine', 
            last_name='SEMWAGA', 
            email='carine@connect.com'
        )
        self.carine.save()

        # Post instance
        self.new_post = Post(
            title='Testing',
            post='This is a testing post.',
            author=self.carine
        )
        self.new_post.save()

        # Comment instance
        self.post_comment = Comment(
            comment='Adding a test comment...',
            post=self.new_post,
            author=self.carine
        )

    # Test instance method
    def test_instance(self):
        self.assertTrue(isinstance(self.post_comment, Comment))
        
    # Test save method
    def test_save(self):
        self.post_comment.save()

    # Test update method
    def test_update(self):
        Comment.objects.filter(id=1).update(comment='Updated comment...')

    # Delete method
    def TearDown(self):
        Author.objects.all().delete()

