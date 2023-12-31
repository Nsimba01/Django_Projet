# Generated by Django 4.2.2 on 2023-06-13 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applipizza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('idComposition', models.AutoField(primary_key=True, serialize=False)),
                ('quantite', models.CharField(max_length=100, verbose_name='la quantité')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applipizza.ingredient')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applipizza.pizza')),
            ],
            options={
                'unique_together': {('ingredient', 'pizza')},
            },
        ),
    ]
