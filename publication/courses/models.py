import os
from http.client import responses
from unicodedata import name
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse






img = 0
img_sub=0
vid = 0
fil = 0
fil_pre=0

def rename_image(instance, filename):
    '''instance here is the user of the profile class '''
    global img
    upload_to = 'image/'
    # recuperer l'extension de l'image et traiter
    #img.png
    extension = filename.split('.')[-1]
    extension = filename.split('.')[-1]
    list = ['jpeg', 'jpg', 'png']
    for elm in list:
        if elm==extension:
            img = img+1
            filename = "course_images/img-{}.{}".format(img, extension)
            return os.path.join(upload_to,  filename)
    return print('format error')


def rename_image_subject(instance, filename):
    '''instance here is the user of the profile class '''
    global img_sub
    upload_to = 'image/'
    # recuperer l'extension de l'image et traiter
    #img.png
    extension = filename.split('.')[-1]
    extension = filename.split('.')[-1]
    list = ['jpeg', 'jpg', 'png']
    for elm in list:
        if elm==extension:
            img_sub = img_sub+1
            filename = "course_images/subject/img-{}.{}".format(img_sub, extension)
            return os.path.join(upload_to,  filename)
    return print('format error')




def rename_image_course(instance, filename):
    '''instance here is the user of the profile class '''
    global img_sub
    upload_to = 'image/'
    # recuperer l'extension de l'image et traiter
    #img.png
    extension = filename.split('.')[-1]
    extension = filename.split('.')[-1]
    list = ['jpeg', 'jpg', 'png']
    for elm in list:
        if elm==extension:
            img_sub = img_sub+1
            filename = "course_images/subject/img-{}.{}".format(img_sub, extension)
            return os.path.join(upload_to,  filename)
    return print('format error')


def rename_video(instance, filename):
    '''instance here is the user of the profile class '''
    global vid 
    upload_to = 'video/'
    vid=vid+1
    # recuperer l'extension de l'image et traiter
    #img.png
    extension = filename.split('.')[-1]
    list = ['mp4', 'mkv']
    for elm in list:

        if elm==extension:
            filename = "course_video/video-.{}".format(extension)
            return os.path.join(upload_to,  filename)
    return print('format error')
        
def rename_file(instance, filename):
    global fil
    '''instance here is the user of the profile class '''
    upload_to = 'file/'
    # recuperer l'extension de l'image et traiter
    #img.png
    extension = filename.split('.')[-1]
    list = ['doc', 'pdf', 'docx']
    for elm in list:
        fil = fil+1
        if elm==extension:
            filename = "course_file/file-{}.{}".format(fil, extension)
            return os.path.join(upload_to,  filename)
    return print('format error')

def rename_present_file(instance, filename):
    global fil_pre
    '''instance here is the user of the profile class '''
    upload_to = 'file/'
    # recuperer l'extension de l'image et traiter
    #img.png
    extension = filename.split('.')[-1]
    list = ['doc', 'pdf', 'docx']
    for elm in list:
        fil_pre = fil_pre+1
        if elm==extension:
            filename = "course_present_file/file-{}.{}".format(fil_pre, extension)
            return os.path.join(upload_to,  filename)
    return print('format error')








# Create your models here.
class Subject(models.Model):
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True) #aide a enlever les espaces entre les mots
    description = models.TextField()
    image = models.ImageField(upload_to=rename_image_subject, blank=True)

    
    # mettre les fonction pour chaque slug
    class Meta:
        ordering = ('name',)
        verbose_name = 'subject'
        verbose_name_plural = 'subjects'

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


 #related_name='subject'(ie c'est le nom de la relation entre Subject et Courses)   
class Course(models.Model):
    
    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE) 
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='course')
    course_id = models.CharField(unique=True, max_length= 40)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to=rename_image_course, blank= True)
    description = models.TextField(max_length=500 )
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
  


class Module(models.Model):
    module_id = models.CharField(unique=True, max_length=40)
    subject =  models.ForeignKey(Subject, on_delete= models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)    #qui a creer ce module/cours 
    course = models.ForeignKey(Course, on_delete= models.CASCADE, related_name='module' ) # related_name pck veut delete entre la table module et course
    name = models.CharField(max_length= 100)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    position = models.PositiveSmallIntegerField(verbose_name= 'chapitre_no') # verbose name(cmt appele ce champ)

    video = models.FileField(upload_to=rename_video, null=True, blank=True, verbose_name="video course")
    present_file = models.FileField(upload_to=rename_present_file, null=True, blank=True, verbose_name="presenting file")
    pdf_course = models.FileField(upload_to=rename_file, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    #fppc =models.FileField(upload_to= "FPPC", null= True, blank= True, verbose_name="fiche de presentation")  # fic pres pc(FPPC)
    #pdf = models.FileField(upload_to= "PDF", null= True, blank= True, verbose_name="cours en pdf")
    
    #order = OrderField(blank=True, for_fields=['course'])


    # class pour ordonner les modules (chap/lesson)
    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("courses:modulelist", kwargs={"slug": self.course.slug, "subject":self.subject.slug})    

    
class Comment(models.Model):
    name_module = models.ForeignKey(Module, null=True, on_delete=models.CASCADE,related_name='comments')
    name_com =models.CharField(max_length=100, blank=True)
    #response = models.ForeignKey('Commentaire',null=True, blank=True, on_delete= models.CASCADE, related_name='reponses')
    #utiliser Commentaire pour faire des reponses
    owner =models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField(max_length=500)
    created =models.DateTimeField(auto_now_add=True) 
    
    #modifier le nom du commentaire
    def save(self, *args, **kwargs):
        self.name_com = slugify("commenter par" + str(self.owner) + "a" + str(self.created))
        super().save(*args, **kwargs)

    #nom a retourner
    def __str__(self):
        return self.name_com 

    #classer les commentaires par date 
    class  Meta:
        ordering = ['-created']   


class  Response(models.Model):
    name_com = models.ForeignKey(Comment, on_delete= models.CASCADE, related_name='responses')  
    body = models.TextField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "reponse a" + str(self.name_com.name_com)     