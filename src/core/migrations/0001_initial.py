# Generated by Django 4.2.4 on 2023-09-04 11:54

import autoslug.fields
import core.utils
import dirtyfields.dirtyfields
from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields
import uuid
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region=None, unique=True, verbose_name='Phone Number')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=core.utils.get_user_slug, unique=True)),
                ('nid', models.CharField(blank=True, max_length=20)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, upload_to=core.utils.get_user_media_path_prefix, verbose_name='Image')),
                ('type', models.CharField(choices=[('UNKNOWN', 'Unknown'), ('PATIENT', 'Patient'), ('DOCTOR', 'Doctor'), ('STAFF', 'Staff')], max_length=20)),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('PLACEHOLDER', 'Placeholder'), ('ACTIVE', 'Active'), ('HIDDEN', 'Hidden'), ('PAUSED', 'Paused'), ('REMOVED', 'Removed')], db_index=True, default='ACTIVE', max_length=20)),
                ('gender', models.CharField(blank=True, choices=[('FEMALE', 'Female'), ('MALE', 'Male'), ('UNKNOWN', 'Unknown'), ('OTHER', 'Other')], default='UNKNOWN', max_length=20)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('NOT_SET', 'Not Set'), ('A+', 'A Positive'), ('A-', 'A Negative'), ('B+', 'B Positive'), ('B-', 'B Negative'), ('AB+', 'Ab Positive'), ('AB-', 'Ab Negative'), ('O+', 'O Positive'), ('O-', 'O Negative')], default='NOT_SET', max_length=10)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('-date_joined',),
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
