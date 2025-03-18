from django.db import models

class ChuyenMuc(models.Model):
    id_chuyen_muc =  models.IntegerField(primary_key=True)
    ten_chuyen_muc = models.CharField(max_length=100)

    def __str__(self):
        return self.ten_chuyen_muc

class TacGia(models.Model):
    id_tac_gia =  models.IntegerField(primary_key=True)
    tac_gia = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.tac_gia

class BaiViet(models.Model):
    id_bai_viet =  models.IntegerField(primary_key=True)
    ngay_xuat_ban = models.DateField()
    tieu_de = models.CharField(max_length=200)
    tac_gia  = models.ForeignKey(TacGia, on_delete=models.CASCADE)
    chuyen_muc = models.ForeignKey(ChuyenMuc, on_delete=models.CASCADE)
    noi_dung = models.TextField()

    def __str__(self):
        return self.tieu_de

class NguoiDung(models.Model):
    id_nguoi_dung =  models.IntegerField(primary_key=True)
    ten_tai_khoan = models.CharField(max_length=100)
    mat_khau = models.CharField(max_length=100)
    email = models.EmailField()
    vai_tro = models.CharField(max_length=100)

    def __str__(self):
        return self.ten_tai_khoan
    