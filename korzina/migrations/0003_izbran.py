# Generated by Django 4.2.7 on 2024-01-17 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('korzina', '0002_korzina_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Izbran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tovar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='korzina.tovar')),
            ],
        ),
    ]
