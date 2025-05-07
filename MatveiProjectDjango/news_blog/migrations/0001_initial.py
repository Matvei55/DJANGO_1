from django.db import migrations, models

class Migration(migrations.Migration):  # <- Класс Migration обязателен!
    initial = True

    dependencies = [
        # Зависимости от других миграций (если есть)
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(...)),
                # ... остальные поля ...
            ],
        ),
    ]