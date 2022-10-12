# Generated by Django 2.2.16 on 2022-10-11 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',), 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following', models.ForeignKey(help_text='Following by', on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='following by')),
                ('user', models.ForeignKey(help_text='Follower', on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='Follower')),
            ],
            options={
                'verbose_name': 'Follow',
                'verbose_name_plural': 'Follows',
                'ordering': ('-id',),
            },
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_user_following_pair'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, following=django.db.models.expressions.F('user')), name='check_self_following'),
        ),
    ]