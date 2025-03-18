from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),  
    #Chuyên Mục
    path('TaoChuyenMuc/', views.TaoChuyenMuc, name='TaoChuyenMuc'),
    path('SuaChuyenMuc/', views.SuaChuyenMuc, name='SuaChuyenMuc'),
    path('XoaChuyenMuc/', views.XoaChuyenMuc, name='XoaChuyenMuc'),
    path('XemChuyenMuc/', views.XemChuyenMuc, name='XemChuyenMuc'),
    #TacGia
    path('ThemTacGia/', views.ThemTacGia, name='ThemTacGia'),
    path('SuaTacGia/', views.SuaTacGia, name='SuaTacGia'),
    path('XoaTacGia/', views.XoaTacGia, name='XoaTacGia'),
    path('XemTacGia/', views.XemTacGia, name='XemTacGia'),
    #BaiVet
    path('TaoBaiViet/', views.TaoBaiViet, name='TaoBaiViet'),
    path('SuaBaiViet/', views.SuaBaiViet, name='SuaBaiViet'),
    path('XoaBaiViet/', views.XoaBaiViet, name='XoaBaiViet'),
    path('XemBaiViet/', views.XemBaiViet, name='XemBaiViet'),
    #NguoiDung
    path('TaoNguoiDung/', views.TaoNguoiDung, name='TaoNguoiDung'),
    path('SuaNguoiDung/', views.SuaNguoiDung, name='SuaNguoiDung'),
    path('XoaNguoiDung/', views.XoaNguoiDung, name='XoaNguoiDung'),
    path('XemNguoiDung/', views.XemNguoiDung, name='XemNguoiDung'),
    
    path('home/', views.home, name='home'),
    
    # #json
    path('api/tacgias', views.apitacgias, name='apitacgias'),
    path('api/chuyenmucs', views.apichuyenmucs, name='apichuyenmucs'),

    
]
