# Generated by Django 2.2.12 on 2021-11-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_auto_20211107_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='department',
            field=models.CharField(choices=[('Accounting/Finance', 'Accounting/Finance'), ('Administration', 'Administration'), ('Agriculture', 'Agriculture'), ('Art / Media', 'Art / Media'), ('Automotive service', 'Automotive service'), ('Aviation/Airport', 'Aviation/Airport'), ('Banking', 'Banking'), ('Engineering', 'Engineering'), ('Hotels, restaurants, service', 'Hotels, restaurants, service'), ('Information technology', 'Information technology'), ('Insurance', 'Insurance'), ('Marketing, Advertising, PR', 'Marketing, Advertising, PR'), ('Medical', 'Medical'), ('Quality control, environment, safety', 'Quality control, environment, safety'), ('Security', 'Security'), ('Tourism/entertainment industry', 'Tourism/entertainment industry'), ('Training courses/Educational programmes', 'Training courses/Educational programmes'), ('Beauty/Aesthetic Medicine', 'Beauty/Aesthetic Medicine'), ('Top management', 'Top management')], default='dep choice', max_length=60),
        ),
    ]
