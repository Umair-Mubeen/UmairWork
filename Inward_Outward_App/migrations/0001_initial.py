# Generated by Django 4.1.3 on 2022-11-12 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_Name', models.CharField(max_length=255)),
                ('Emp_Pwd', models.CharField(max_length=255)),
                ('Emp_Email', models.CharField(max_length=255)),
                ('Emp_Age', models.IntegerField()),
                ('Emp_Designation', models.CharField(max_length=255)),
                ('EmpAddress', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sender_Name', models.CharField(max_length=255)),
                ('Sender_Letter_Number', models.CharField(max_length=255)),
                ('Sender_Letter_Date', models.DateField(null=True)),
                ('Sender_Letter_Subject', models.CharField(max_length=255)),
                ('Sender_Letter_Type', models.CharField(max_length=255)),
                ('Sender_Letter_Compliance_Date', models.DateField(null=True)),
                ('Office_Letter_Number', models.CharField(max_length=255)),
                ('Office_Letter_Date', models.DateField(null=True)),
                ('Office_Letter_Marked_To', models.CharField(max_length=255)),
                ('Officer_Remarks', models.CharField(max_length=255)),
                ('Office_Compliance_Status', models.CharField(max_length=255)),
            ],
        ),
    ]