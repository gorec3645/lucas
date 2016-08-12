# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-11 11:18
from __future__ import unicode_literals

import assessment.validator
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(validators=[assessment.validator.validate_point])),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Expert')),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(max_length=60)),
                ('category', models.CharField(choices=[('VS', 'Свойства зрительного анализаторов'), ('HR', 'Свойства слухового анализатора'), ('SM', 'Свойства обонятельного анализатора'), ('TM', 'Свойства температурного анализатора'), ('TC', 'Свойства тактильного анализатора'), ('AT', 'Свойства внимания'), ('MM', 'Свойства памяти'), ('TN', 'Свойства мышления'), ('RT', 'Сенсомоторные реакции'), ('VM', 'Свойства зрительного, двигательного, вестибулярного, слухового анализаторов'), ('VH', 'Свойства зрительного, слухового, кожного, двигательного анализаторов'), ('AI', 'Свойства интеллекта'), ('VV', 'Свойства зрительного и вестибулярного анализаторов'), ('HN', 'Свойства высшей нервной деятельности'), ('EM', 'Свойства эмоционально-волевой и мотивационной сфер')], max_length=60)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='assessment',
            name='quality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.Quality'),
        ),
        migrations.AlterUniqueTogether(
            name='assessment',
            unique_together=set([('quality', 'expert')]),
        ),
    ]