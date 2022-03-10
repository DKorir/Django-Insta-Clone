# Generated by Django 4.0.3 on 2022-03-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theinsta', '0003_post_likes_alter_post_title_tag_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=255),
        ),
    ]
