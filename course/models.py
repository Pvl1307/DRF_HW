from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Course title', **NULLABLE)
    picture = models.ImageField(upload_to='course/', verbose_name='Course picture', **NULLABLE)
    description = models.TextField(verbose_name='Course description', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name='Lesson title', **NULLABLE)
    description = models.TextField(verbose_name='Lesson description', **NULLABLE)
    picture = models.ImageField(upload_to='course/lesson', **NULLABLE)
    video_url = models.URLField(max_length=500, verbose_name='Lesson video URL', **NULLABLE)

    def __str__(self):
        return f'{self.title}: {self.video_url}'

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
