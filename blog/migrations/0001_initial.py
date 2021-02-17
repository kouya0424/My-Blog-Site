from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models. AutoField(auto_created=True, primary_key=True,
                                         serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('text', models.TextField(default='')),
                ('author', models.CharField(default='', max_length=30)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
