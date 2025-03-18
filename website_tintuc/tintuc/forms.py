from django import forms
from  .models import BaiViet, ChuyenMuc, TacGia, NguoiDung

#Chuyên Mục
class CreateNewChuyenMuc(forms.ModelForm):
    class Meta : 
        model = ChuyenMuc
        fields = '__all__'
        
class UpdateChuyenMuc(forms.Form):
    id_chuyen_muc =  forms.CharField(max_length=10)
    ten_chuyen_muc = forms.CharField(max_length=100)

class DeleteChuyenMuc(forms.Form):
    id_chuyen_muc =  forms.CharField(max_length=10)
    
class ViewChuyenMuc(forms.ModelForm):
    class Meta : 
        model = ChuyenMuc
        fields = '__all__'

#TacGia
class NewTacGia(forms.ModelForm):
    class Meta : 
        model = TacGia
        fields = '__all__'
        
class UpdateTacGia(forms.Form):
    id_tac_gia = forms.CharField(max_length=10)
    tac_gia = forms.CharField(max_length=100)
    email = forms.EmailField()
    
class DeleteTacGia(forms.Form):
    id_tac_gia = forms.CharField(max_length=10)

class ViewTacGia(forms.ModelForm):
    class Meta : 
        model = TacGia
        fields = '__all__'
        
#BaiViet
class CreateNewBaiViet(forms.ModelForm):
    class Meta : 
        model = BaiViet
        fields = '__all__'

class UpdateBaiViet(forms.Form):
   id_bai_viet = forms.CharField(max_length=10)
   ngay_xuat_ban= forms.DateField()
   tieu_de = forms.CharField(max_length=200)
   noi_dung = forms.CharField(widget=forms.Textarea)
   
class DeleteBaiViet(forms.Form):
    id_bai_viet = forms.CharField(max_length=10)

class ViewBaiViet(forms.ModelForm):
    class Meta : 
        model = BaiViet
        fields = '__all__'
        
#NguoiDung
class CreateNewNguoiDung(forms.ModelForm):
    class Meta : 
        model = NguoiDung
        fields = '__all__'
        
class UpdateNguoiDung(forms.Form):
    id_nguoi_dung =  forms.CharField(max_length=10)
    ten_tai_khoan = forms.CharField(max_length=100)
    mat_khau = forms.CharField(max_length=100)
    email =forms.EmailField()
    vai_tro=forms.CharField(max_length=100)
    
class DeleteNguoiDung(forms.Form):
    id_nguoi_dung = forms.CharField(max_length=10)

class ViewNguoiDung(forms.ModelForm):
    class Meta : 
        model = NguoiDung
        fields = '__all__'   
    