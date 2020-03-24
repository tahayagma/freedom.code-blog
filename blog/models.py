from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField

class CreatePost(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField()
    publishing_date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(null=True,blank=True)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,max_length=160)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detailpage',kwargs={'slug':self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı','i'))
        unique_slug =slug
        counter = 1
        while CreatePost.objects.filter(slug=unique_slug).exists():
            unique_slug ="{}-{}".format(slug,counter)
            counter += 1
        return unique_slug

    def save(self,*args,**kwargs):
        self.slug = self.get_unique_slug()
        super().save(*args,**kwargs)

    def get_tags_url(self):
        return reverse('taG' ,kwargs={'tag',self.tag})

    class Meta:
        ordering = ['-publishing_date']


class MakeComment(models.Model):
    Comments = models.ForeignKey('CreatePost', related_name='comments', on_delete=models.CASCADE)
    nameSurname = models.CharField(max_length=100)
    email = models.EmailField()
    Content =models.TextField()
    publishing_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-publishing_date']