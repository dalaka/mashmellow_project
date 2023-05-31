# Generated by Django 3.2.7 on 2023-05-30 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('articles', '0001_schema__initial_model_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='author', to='author.author'),
            preserve_default=False,
        ),
    ]
