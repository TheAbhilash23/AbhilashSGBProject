# Generated by Django 4.0 on 2022-07-20 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudding', '0007_delete_odb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Odb',
            fields=[
                ('custid', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_risk', models.IntegerField()),
                ('status', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('credit_history', models.IntegerField()),
                ('purpose', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('savings', models.IntegerField()),
                ('employment_duration', models.IntegerField()),
                ('installment_rate', models.IntegerField()),
                ('personal_status_sex', models.IntegerField()),
                ('other_debtors', models.IntegerField()),
                ('present_residence', models.IntegerField()),
                ('property_type', models.IntegerField()),
                ('age', models.IntegerField()),
                ('other_installment_plans', models.IntegerField()),
                ('housing', models.IntegerField()),
                ('number_credits', models.IntegerField()),
                ('job', models.IntegerField()),
                ('people_liable', models.IntegerField()),
                ('telephone', models.IntegerField()),
                ('foreign_worker', models.IntegerField()),
            ],
        ),
    ]
