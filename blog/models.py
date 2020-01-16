from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class PostCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'post_category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:post_list_by_category', kwargs={
            'slug': self.slug
        })


class PostQuerySet(models.query.QuerySet):
    def status(self):
        return self.filter(status=1)

    def category(self, query):
        return self.filter(status=1, category=query)

    def search(self, query):
        lookups = (Q(title__icontains=query) |
                   Q(author__icontains=query) |
                   Q(content__icontains=query) |
                   Q(category__name__icontains=query)
                   )

        return self.filter(lookups).distinct()


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().status()

    def get_by_id(self, id):
        # Product.objects == self.get_queryset()
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().status().search(query)

    def category(self, query):
        return self.get_queryset().category(query)


class Post(models.Model):
    category = models.ForeignKey(
        PostCategory, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    objects = PostManager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
