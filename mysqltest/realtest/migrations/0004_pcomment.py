# Generated by Django 3.1.3 on 2021-01-11 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtest', '0003_auto_20210110_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('content', models.TextField(max_length=300, null=True)),
                ('make_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtest.product')),
            ],
        ),
    ]