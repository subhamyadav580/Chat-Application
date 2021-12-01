# Generated by Django 3.2.9 on 2021-12-01 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_message_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=255)),
                ('room_password', models.CharField(max_length=15)),
                ('room_created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('room_created_date',),
            },
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('message_time',)},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='content',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='date_added',
            new_name='message_time',
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.room'),
        ),
    ]
