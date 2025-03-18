from django.contrib import admin

from .models import ChuyenMuc , TacGia, BaiViet, NguoiDung

# Register your models here.
admin.site.register(ChuyenMuc)
admin.site.register(TacGia)
admin.site.register(BaiViet)
admin.site.register(NguoiDung)
