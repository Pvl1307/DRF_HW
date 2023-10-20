from django.contrib import admin

from course.models import Course, Lesson, Payments, Subscription

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Payments)
admin.site.register(Subscription)
