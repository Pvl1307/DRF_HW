import logging

from celery import shared_task
from django.core.mail import send_mail

from config import settings
from course.models import Subscription

logger = logging.getLogger(__name__)


@shared_task
def send_mail_about_updates(course_id):
    object_subs = Subscription.objects.filter(course=course_id)
    for sub in object_subs:
        try:
            send_mail(
                subject=f'Course {sub.course.title} was updated!',
                message=f'Course {sub.course.title} was updated! Check what author did!)',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[sub.user.email],
                fail_silently=False,
            )

            logger.info(f'Mail sent to {sub.user.email}')
        except Exception as e:
            logger.error(f'Failed to send email: {str(e)}')
