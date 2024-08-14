# Generated by Django 4.2 on 2024-07-31 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birt_date', models.DateField()),
                ('level', models.IntegerField(default=1)),
                ('picture', models.ImageField(upload_to='trainer_images')),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('T', 'Tierra'), ('A', 'Agua'), ('L', 'Lagartija'), ('F', 'Fuego'), ('P', 'Planta'), ('Fu', 'Futblista'), ('E', 'Eléctrico')], max_length=30)),
                ('weight', models.IntegerField(default=1)),
                ('height', models.IntegerField(default=1)),
                ('picture', models.ImageField(upload_to='pokemon_images')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokedex.trainer')),
            ],
        ),
    ]
