from django.db import models

# Author Model Class
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

# Post Model Class
class Post(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pk']

# Comment Model Class
class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post)
    author = models.ForeignKey(Author)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'self.author.name Post'

    class Meta:
        ordering = ['-pk']