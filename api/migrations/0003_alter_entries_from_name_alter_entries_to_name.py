# Generated by Django 4.1.7 on 2024-02-24 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_userlogin_is_user_entries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='from_name',
            field=models.ForeignKey(limit_choices_to={'is_user': True}, on_delete=django.db.models.deletion.CASCADE, related_name='from_entries', to='api.userlogin'),
        ),
        migrations.AlterField(
            model_name='entries',
            name='to_name',
            field=models.ForeignKey(limit_choices_to={'is_user': False}, on_delete=django.db.models.deletion.CASCADE, related_name='to_entries', to='api.userlogin'),
        ),
    ]
