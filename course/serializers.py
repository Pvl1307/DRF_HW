from rest_framework import serializers

from course.models import Course, Lesson, Payments, Subscription
from course.services import create_price
from course.validators import forbidden_url


class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField(validators=[forbidden_url])
    payment_link = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = '__all__'

    @staticmethod
    def get_payment_link(instance):
        return create_price('Lesson', Lesson.objects.get(pk=instance.pk))


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lessons', many=True, read_only=True)
    is_subscribed = SubscriptionSerializer(source='subs', many=True, read_only=True)
    payment_link = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    @staticmethod
    def get_num_lessons(instance):
        return instance.lessons.count()

    @staticmethod
    def get_payment_link(instance):
        return create_price('Course', Course.objects.get(pk=instance.pk))


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
