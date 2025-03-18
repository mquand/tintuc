# Generated by Django 5.0.4 on 2024-06-09 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChuyenMuc',
            fields=[
                ('id_chuyen_muc', models.IntegerField(primary_key=True, serialize=False)),
                ('ten_chuyen_muc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NguoiDung',
            fields=[
                ('id_nguoi_dung', models.IntegerField(primary_key=True, serialize=False)),
                ('ten_tai_khoan', models.CharField(max_length=100)),
                ('mat_khau', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('vai_tro', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TacGia',
            fields=[
                ('id_tac_gia', models.IntegerField(primary_key=True, serialize=False)),
                ('tac_gia', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='BaiViet',
            fields=[
                ('id_bai_viet', models.IntegerField(primary_key=True, serialize=False)),
                ('ngay_xuat_ban', models.DateField()),
                ('tieu_de', models.CharField(max_length=200)),
                ('noi_dung', models.TextField()),
                ('chuyen_muc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tintuc.chuyenmuc')),
                ('tac_gia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tintuc.tacgia')),
            ],
        ),
    ]
