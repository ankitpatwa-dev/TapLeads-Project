# Generated by Django 3.2.8 on 2021-12-21 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(max_length=200, null=True)),
                ('full_name', models.CharField(max_length=200, null=True)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('middle_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('company', models.CharField(max_length=200, null=True)),
                ('designation', models.CharField(max_length=200, null=True)),
                ('emailid', models.EmailField(max_length=200, null=True)),
                ('aadhar', models.CharField(max_length=12, null=True)),
                ('pan_card', models.CharField(max_length=10, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('department', models.CharField(max_length=200, null=True)),
                ('university', models.CharField(max_length=200, null=True)),
                ('degree', models.CharField(max_length=200, null=True)),
                ('passing_year', models.CharField(max_length=200, null=True)),
                ('college', models.CharField(max_length=200, null=True)),
                ('linkedin', models.URLField(null=True)),
                ('facebook', models.URLField(null=True)),
                ('instagram', models.URLField(null=True)),
                ('industry', models.CharField(max_length=200, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('pin_code', models.CharField(max_length=200, null=True)),
                ('key_skills', models.CharField(max_length=200, null=True)),
                ('total_experience', models.CharField(max_length=200, null=True)),
                ('years_in_business', models.CharField(max_length=200, null=True)),
                ('cin_no', models.CharField(max_length=200, null=True)),
                ('turnover', models.CharField(default='0', max_length=200, null=True)),
                ('date_of_incorporation', models.CharField(max_length=200, null=True)),
                ('employees', models.CharField(max_length=200, null=True)),
                ('ctc', models.CharField(max_length=200, null=True)),
                ('notes', models.CharField(max_length=200, null=True)),
                ('remarks', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='predefined', max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='contacts_app.contact')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13, null=True)),
                ('total_limits', models.IntegerField(default=0)),
                ('viewed', models.IntegerField(default=0)),
                ('current_method', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='contacts_app.method')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
                ('contact', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='contacts_app.contact')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SaveSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_criteria', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('weightage', models.IntegerField(default=0)),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts_app.method')),
            ],
        ),
    ]
