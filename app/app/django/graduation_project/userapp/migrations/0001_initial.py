# Generated by Django 2.2.4 on 2019-10-16 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('algorithm_id', models.AutoField(primary_key=True, serialize=False, verbose_name='알고리즘 번호')),
                ('name', models.CharField(max_length=255, verbose_name='알고리즘 이름')),
            ],
            options={
                'db_table': 'tb_algorithm',
                'ordering': ['algorithm_id'],
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False, verbose_name='문제 번호')),
                ('name', models.CharField(max_length=255, verbose_name='문제 이름')),
                ('submit', models.IntegerField(verbose_name='제출')),
                ('submit_people', models.IntegerField(verbose_name='제출한 사람')),
                ('accept_people', models.IntegerField(verbose_name='맞은 사람')),
                ('average_attempt', models.FloatField(verbose_name='평균 시도')),
                ('accept', models.IntegerField(verbose_name='맞았습니다')),
                ('wrong', models.IntegerField(verbose_name='틀렸습니다')),
                ('time_over', models.IntegerField(verbose_name='시간 초과')),
                ('memory_over', models.IntegerField(verbose_name='메모리 초과')),
                ('output_over', models.IntegerField(verbose_name='출력 초과')),
                ('output_type_error', models.IntegerField(verbose_name='출력 형식')),
                ('runtime_error', models.IntegerField(verbose_name='런타임 에러')),
                ('compile_error', models.IntegerField(verbose_name='컴파일 에러')),
                ('accept_proportion', models.FloatField(verbose_name='정답 비율')),
                ('accept_people_proportion', models.FloatField(verbose_name='정답자 비율')),
                ('algorithm_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='userapp.Algorithm')),
            ],
            options={
                'db_table': 'tb_problem',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='사용자 이름')),
                ('rating', models.FloatField(verbose_name='평가 점수')),
                ('last_update', models.DateTimeField(verbose_name='레이팅 변동 날짜')),
            ],
            options={
                'db_table': 'tb_user',
                'ordering': ['-rating', 'last_update'],
            },
        ),
        migrations.CreateModel(
            name='UserSolvedProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.Problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.User')),
            ],
            options={
                'db_table': 'tb_user_solved_problem',
            },
        ),
        migrations.CreateModel(
            name='UserFailedProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.Problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.User')),
            ],
            options={
                'db_table': 'tb_user_failed_problem',
            },
        ),
    ]