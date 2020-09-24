# Generated by Django 2.1.5 on 2020-02-14 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('courts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectedCourt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timein', models.DateTimeField()),
                ('timeout', models.DateTimeField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courts.Court')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
    ]