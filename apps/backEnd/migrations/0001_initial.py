# Generated by Django 2.2.2 on 2020-03-04 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicValidators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NumUsersConnected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numUsers', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
                ('superUser', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('spam', models.BooleanField(default=False)),
                ('userPostsFK', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='postUserFK', to='backEnd.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('spam', models.BooleanField(default=False)),
                ('postCommentsFK', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='commentsPostFK', to='backEnd.Posts')),
                ('userCommentFK', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='commentsUserFK', to='backEnd.Users')),
            ],
        ),
    ]
