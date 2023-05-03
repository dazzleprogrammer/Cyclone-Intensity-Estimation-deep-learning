# Generated by Django 3.2.8 on 2022-02-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intensity_app', '0005_auto_20220223_2107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stormdata',
            options={'ordering': ['storm_name', '-storm_id']},
        ),
        migrations.AlterModelOptions(
            name='stormtrack',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='stormdata',
            name='category',
        ),
        migrations.RemoveField(
            model_name='stormdata',
            name='date',
        ),
        migrations.RemoveField(
            model_name='stormdata',
            name='description',
        ),
        migrations.RemoveField(
            model_name='stormdata',
            name='intensity',
        ),
        migrations.RemoveField(
            model_name='stormdata',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='stormdata',
            name='longitude',
        ),
        migrations.AddField(
            model_name='stormtrack',
            name='category',
            field=models.IntegerField(choices=[(1, 'Tropical Depression'), (2, 'Tropical Storm'), (3, 'Category 1'), (4, 'Category 2'), (5, 'Category 3'), (6, 'Category 4'), (7, 'Category 5')], default=1),
        ),
        migrations.AddField(
            model_name='stormtrack',
            name='category_labels',
            field=models.IntegerField(choices=[(1, 'Tropical Depression'), (2, 'Tropical Storm'), (3, 'Category 1'), (4, 'Category 2'), (5, 'Category 3'), (6, 'Category 4'), (7, 'Category 5')], default=1),
        ),
        migrations.AddField(
            model_name='stormtrack',
            name='labels',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
