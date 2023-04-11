from django.db import models
from django.contrib.auth.models import User

# Create your models here.
SECURITY_QUESTIONS = (
    ('first_pet', 'What was the name of your first pet?'),
    ('birth_city', 'In what city were you born?'),
    ('mother_maiden', "What is your mother's maiden name?"),
    ('first_school', 'What was the name of your first school?'),
    ('favorite_color', 'What is your favorite color?'),
)

class SecurityQuestion(models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city_town = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    full_name = models.CharField(max_length=50, blank=True)
    security_question = models.CharField(max_length=100, choices=SECURITY_QUESTIONS, default='')  
    security_answer = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'Profile for {self.user.username}'
    
