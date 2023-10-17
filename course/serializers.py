from rest_framework import serializers

from course.models import Course, Lesson, Payments, Subscription
from course.services import get_link
from course.validators import forbidden_url


class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField(validators=[forbidden_url])

    class Meta:
        model = Lesson
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lessons', many=True, read_only=True)
    is_subscribed = SubscriptionSerializer(source='subs', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    @staticmethod
    def get_num_lessons(instance):
        return instance.lessons.count()


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class PaymentRetrieveSerializer(serializers.ModelSerializer):
    payment_link = serializers.SerializerMethodField()

    class Meta:
        model = Payments
        fields = '__all__'

    @staticmethod
    def get_payment_link(instance):
        return get_link(instance)


class PaymentSuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ['amount', 'is_paid']
