# Generated by Django 4.2.5 on 2023-10-04 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0003_alter_lesson_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Payment Date')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('way_of_payment', models.CharField(choices=[('cash', 'Cash'), ('amount', 'Amount')], max_length=10, verbose_name='Way of Payment')),
                ('paid_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='course.course', verbose_name='Paid Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]
