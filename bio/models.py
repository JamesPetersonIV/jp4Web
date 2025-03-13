from django.db import models

#Embeds
from embed_video.fields import EmbedVideoField

# Create your models here.
class Literature(models.Model):
    #category
    CATEGORY = (
        ('Novel', 'Novel'),
        ('Comic Book', 'Comic Book'),
        ('Magazine', 'Magazine'),
        ('Flyer', 'Flyer'),
        ('Essay', 'Essay'),
    ) 
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="images", blank=True, null=True)
    summary = models.TextField()
    #will be able to select from contents in CATEGORY
    category = models.CharField(max_length=200, default=False,blank=True, choices=CATEGORY)
    pdf = models.FileField(upload_to='pdf', blank = True, null=True)
    published_date = models.DateField(blank=True, null=True)

    slug = models.SlugField(max_length=50)

    class Meta:
        #database name
        verbose_name_plural = 'Literature'
    def __str__(self):
        return self.title

class Artwork(models.Model):
    SERIES = (
        ('Self-Portraits', 'Self-Portraits'),
        ('Characters', 'Characters'),
        ('Sketches', 'Sketches'),
        ('Mixed-Media', 'Mixed-Media'),
        ('Hatching','Hatching'),
        ('Portraits','Portraits'),
        ('Imagined Portaits', 'Imagined Portraits'),
    )

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="series", blank=True, null=True)
    summary = models.TextField()
    entry = models.CharField(max_length=200, default=False, blank=True, choices=SERIES)
    slug = models.SlugField(max_length=50)
    completed_date = models.DateField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Works of Art'
    def __str__(self):
        return self.name


class Visual(models.Model):
    
    video = models.CharField(max_length=100)
    link = EmbedVideoField()
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Visuals'
    def __str__(self):
        return self.video
    

