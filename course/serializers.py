from rest_framework import serializers

from course.models import Course, Lesson, Payments


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lessons', many=True)

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
