from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
# order and rename image
vid1 = 1
def rename_image(instance, filename):
    '''instance here is the user of the profile class '''
    upload_to = 'image/'
    # recuperer l'extension de l'image et traiter
    #img.png
    extension = filename.split('.')[-1]
    if instance.user.username:
        filename = "profile_image/{}.{}".format(instance.user.username, extension)
    return os.path.join(upload_to,  filename)


def rename_video(instance, filename):
    '''instance here is the user of the profile class '''
    global vid1
    upload_to = 'video/'
    
    # recuperer l'extension de l'image et traiter
    #img.png
    extension = filename.split('.')[-1]
    list = ['mp4', 'mkv']
    for elm in list:
        if elm==extension:
            vid1 = vid1+1
            filename = "default/video-{}.{}".format(vid1, extension)
            return os.path.join(upload_to,  filename)
    return os.path.join(upload_to,  filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150, blank=True)
    profile_image = models.ImageField(upload_to=rename_image, blank=True)
    student = 'student'
    publisher = 'publisher'

    type_user = [
        (student, 'student'), (publisher, 'publisher')
    ]

    type_profile = models.CharField(max_length=100, choices=type_user, default=student)

    def __str__(self):
        return self.user.username
    

class videoDef(models.Model):
    video = models.FileField(upload_to=rename_video, null=True, blank=True, verbose_name="video_default")