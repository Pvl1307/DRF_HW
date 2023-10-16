from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Course title', **NULLABLE)
    picture = models.ImageField(upload_to='course/', verbose_name='Course picture', **NULLABLE)
    description = models.TextField(verbose_name='Course description', **NULLABLE)
    price = models.IntegerField(verbose_name='Price')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}.Price-{self.price}'

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course', **NULLABLE, related_name='subs')
    subscription = models.BooleanField(default=False, verbose_name='Subscription')

    def __str__(self):
        return f'{self.user} subscription on {self.course}: {self.subscription}'

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, related_name='lessons')

    title = models.CharField(max_length=200, verbose_name='Lesson title', **NULLABLE)
    description = models.TextField(verbose_name='Lesson description', **NULLABLE)
    picture = models.ImageField(upload_to='course/lesson', **NULLABLE)
    video_url = models.URLField(max_length=500, verbose_name='Lesson video URL', **NULLABLE)
    price = models.IntegerField(verbose_name='Price')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.pk} {self.course}: {self.title}: {self.owner}. Price-{self.price}'

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'


class Payments(models.Model):
    PAYMENT_CHOICES = (
        ('cash', 'Cash'),
        ('transfer', 'Transfer'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', **NULLABLE)
    payment_date = models.DateTimeField(auto_now_add=True, **NULLABLE, verbose_name='Payment Date')

    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, related_name='course')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, related_name='lesson')

    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')
    way_of_payment = models.CharField(max_length=10, choices=PAYMENT_CHOICES, verbose_name='Way of Payment')

    def __str__(self):
        return f'{self.user} paid for {self.paid_course if self.paid_course else self.paid_lesson}: {self.payment_date}'

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
