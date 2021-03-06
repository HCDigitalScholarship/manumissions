# Generated by Django 3.0.7 on 2020-07-24 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_document_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='date_of_Manumission_Signing',
        ),
        migrations.AddField(
            model_name='document',
            name='date_of_Manumission_Signing',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='Age_Freed',
            field=models.CharField(help_text='Age when freedom occured', max_length=3, null=True, verbose_name='Age_Freed'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Age_Listed',
            field=models.CharField(help_text='Age listed on the Manumission Document', max_length=3, null=True, verbose_name='Age_Listed'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Year_Manumitted',
            field=models.CharField(help_text='Year when freedom occured', max_length=4, null=True, verbose_name='Year Manumission took effect'),
        ),
    ]
