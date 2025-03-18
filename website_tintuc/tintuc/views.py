from django.shortcuts import render
from django.http import HttpResponse 
from django.http import JsonResponse
from .serializers import*
from .models import ChuyenMuc , TacGia, BaiViet, NguoiDung
from .forms import *
# Create your views here.

def index(request):
    return HttpResponse('hello xin chafo quan')

#Chuyên Mục-/-/-/--/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
def TaoChuyenMuc(request):
    if request.method == 'POST':
        form = CreateNewChuyenMuc(request.POST)
        if form.is_valid():  
            form.save()
            return HttpResponse('success')
        else : 
            return HttpResponse(form.errors.as_text())  
    form = CreateNewChuyenMuc()
    return render(request, 'ChuyenMuc/NewChuyenMuc.html', {'form': form})

def SuaChuyenMuc(request):    
    if request.method == 'POST':
        form = UpdateChuyenMuc(request.POST)
        if form.is_valid(): 
            id_chuyen_muc = form.cleaned_data['id_chuyen_muc']
            ten_chuyen_muc = form.cleaned_data['ten_chuyen_muc'] 
            ChuyenMuc.objects.filter(id_chuyen_muc=id_chuyen_muc).update(ten_chuyen_muc=ten_chuyen_muc)
            return HttpResponse(' Update success')  
        else : 
            return HttpResponse(form.errors.as_text())
    form = UpdateChuyenMuc()
    return render(request, 'ChuyenMuc/SuaChuyenMuc.html', {'form': form})

def XoaChuyenMuc(request):    
    if request.method == 'POST':
        form = DeleteChuyenMuc(request.POST)
        if form.is_valid(): 
            id_chuyen_muc = form.cleaned_data['id_chuyen_muc']
            ChuyenMuc.objects.filter(id_chuyen_muc=id_chuyen_muc).delete()
            return HttpResponse('Delete success')  
    form = DeleteChuyenMuc()
    return render(request, 'ChuyenMuc/XoaChuyenMuc.html', {'form': form})

def XemChuyenMuc(request):
    chuyenmuc = ChuyenMuc.objects.all()
    return render(request, 'ChuyenMuc/XemChuyenMuc.html', {'chuyenmuc': chuyenmuc})  
    
#TacGia-/-/-/--/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def ThemTacGia(request): 
    if request.method == 'POST':
        form = NewTacGia(request.POST)
        if form.is_valid():  
            form.save()
            return HttpResponse('success')  
        else : 
            return HttpResponse(form.errors.as_text())
    form = NewTacGia()
    return render(request, 'TacGia/ThemTacGia.html', {'form': form})

def SuaTacGia(request):    
    if request.method == 'POST':
        form = UpdateTacGia(request.POST)
        if form.is_valid(): 
            id_tac_gia = form.cleaned_data['id_tac_gia']
            tac_gia = form.cleaned_data['tac_gia'] 
            email = form.cleaned_data['email'] 
            TacGia.objects.filter(id_tac_gia=id_tac_gia).update(tac_gia=tac_gia,email=email)
            return HttpResponse(' Update success')  
        else : 
            return HttpResponse(form.errors.as_text())
    form = UpdateTacGia()
    return render(request, 'TacGia/SuaTacGia.html', {'form': form})

def XoaTacGia(request):    
    if request.method == 'POST':
        form = DeleteTacGia(request.POST)
        if form.is_valid(): 
            id_tac_gia = form.cleaned_data['id_tac_gia']
            TacGia.objects.filter(id_tac_gia =id_tac_gia ).delete()
            return HttpResponse('Delete success')  
    form = DeleteTacGia()
    return render(request, 'TacGia/XoaTacGia.html', {'form': form})

def XemTacGia(request):
    tacgia = TacGia.objects.all()
    return render(request, 'TacGia/XemDSTacGia.html', {'tacgia': tacgia})

#BaiViet-/-/-/--/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
def TaoBaiViet(request):
    if request.method == 'POST':
        form = CreateNewBaiViet(request.POST)
        if form.is_valid():  
            form.save()
            return HttpResponse('success')  
        else : 
            return HttpResponse(form.errors.as_text())
    tacgia = TacGia.objects.all()
    chuyenmuc = ChuyenMuc.objects.all()
    form = CreateNewBaiViet()
    return render(request, 'BaiViet/TaoBaiViet.html', {'form': form, 'tacgia': tacgia, 'chuyenmuc':chuyenmuc})
    
def SuaBaiViet(request):    
    if request.method == 'POST':
        form = UpdateBaiViet(request.POST)
        if form.is_valid(): 
            id_bai_viet = form.cleaned_data['id_bai_viet']
            ngay_xuat_ban = form.cleaned_data['ngay_xuat_ban'] 
            tieu_de = form.cleaned_data['tieu_de'] 
            noi_dung =form.cleaned_data['noi_dung'] 
            BaiViet.objects.filter(id_bai_viet =id_bai_viet ).update(ngay_xuat_ban=ngay_xuat_ban,tieu_de=tieu_de,noi_dung=noi_dung)
            return HttpResponse(' Update success') 
        else : 
            return HttpResponse(form.errors.as_text()) 
    tacgia = TacGia.objects.all()
    chuyenmuc = ChuyenMuc.objects.all()
    form = UpdateBaiViet()
    return render(request, 'BaiViet/SuaBaiViet.html', {'form': form,'tacgia': tacgia, 'chuyenmuc':chuyenmuc})

def XoaBaiViet(request):    
    if request.method == 'POST':
        form = DeleteBaiViet(request.POST)
        if form.is_valid(): 
            id_bai_viet = form.cleaned_data['id_bai_viet']
            BaiViet.objects.filter(id_bai_viet =id_bai_viet ).delete()
            return HttpResponse('Delete success')  
    form = DeleteBaiViet()
    return render(request, 'BaiViet/XoaBaiViet.html', {'form': form})

def XemBaiViet(request):
    baiviet= BaiViet.objects.all()
    return render(request, 'BaiViet/XemBaiViet.html', {'baiviet': baiviet})

#NguoiDung-/-/-/--/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def TaoNguoiDung(request):
    if request.method == 'POST':
        form = CreateNewNguoiDung(request.POST)
        if form.is_valid():  
            form.save()
            return HttpResponse('success')
        else : 
            return HttpResponse(form.errors.as_text())  
    form = CreateNewNguoiDung()
    return render(request, 'NguoiDung/TaoNguoiDung.html', {'form': form})

def SuaNguoiDung(request):    
    if request.method == 'POST':
        form = UpdateNguoiDung(request.POST)
        if form.is_valid(): 
            id_nguoi_dung = form.cleaned_data['id_nguoi_dung']
            vai_tro = form.cleaned_data['vai_tro']
            ten_tai_khoan = form.cleaned_data['ten_tai_khoan'] 
            email = form.cleaned_data['email'] 
            mat_khau= form.cleaned_data['mat_khau']
            NguoiDung.objects.filter(id_nguoi_dung=id_nguoi_dung).update(ten_tai_khoan=ten_tai_khoan,email=email,mat_khau=mat_khau, vai_tro=vai_tro)
            return HttpResponse(' Update success')  
        else : 
            return HttpResponse(form.errors.as_text())
    form = UpdateNguoiDung()
    return render(request, 'NguoiDung/SuaNguoiDung.html', {'form': form})

def XoaNguoiDung(request):    
    if request.method == 'POST':
        form = DeleteNguoiDung(request.POST)
        if form.is_valid(): 
            id_nguoi_dung = form.cleaned_data['id_nguoi_dung']
            NguoiDung.objects.filter( id_nguoi_dung = id_nguoi_dung ).delete()
            return HttpResponse('Delete success')  
    form = DeleteNguoiDung()
    return render(request, 'NguoiDung/XoaNguoiDung.html', {'form': form})

def XemNguoiDung(request):
    nguoidung = NguoiDung.objects.all()
    return render(request, 'NguoiDung/XemDSNguoiDung.html', {'nguoidung': nguoidung})

#search
def home(request):
    TuKhoa = request.GET.get('TuKhoa')
    tieudes = []
    if TuKhoa:
        tieudes = BaiViet.objects.filter(tieu_de__icontains=TuKhoa)
    return render(request, 'home/home.html', {'tieudes': tieudes, 'TuKhoa': TuKhoa})



# #json 
def apitacgias(request):
    queryset = TacGia.objects.all()
    data = TacGiaSerializer(queryset, many=True)
    return JsonResponse(data.data,safe=False)

def apichuyenmucs(request):
    queryset = ChuyenMuc.objects.all()
    data = ChuyenMucSerializer(queryset, many=True)
    return JsonResponse(data.data,safe=False)