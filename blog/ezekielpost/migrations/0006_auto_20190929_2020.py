# Generated by Django 2.2.2 on 2019-09-29 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezekielpost', '0005_auto_20190929_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='post/personal.png', upload_to='post/'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_image_alt',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
