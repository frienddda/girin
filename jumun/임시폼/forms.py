from django import forms
from .models import jumun_T

class RegisterForm(forms.Form):
    jumun_id = forms.CharField(
        error_messages={'required':"주문자id를 입력하세요."},
        max_length = 30, label = "주문자id"
    )
    jumun_name = forms.CharField(
        error_messages={'required':"주문자를 입력하세요."},
        max_length = 30, label = "주문자"
    )
    consumer = forms.CharField(
        error_messages={'required':"소비자를 입력하세요."},
        max_length = 30, label = "소비자"
    )
    brand = forms.CharField(
        error_messages={'required':"브랜드를 입력하세요."},
        max_length = 30, label = "브랜드"
    )
    prd_name = forms.CharField(
        error_messages={'required':"상품명을 입력하세요."},
        max_length = 30, label = "상품명"
    )
    option = forms.CharField(
        error_messages={'required':"옵션을 입력하세요."},
        max_length = 30, label = "옵션"
    )
    price = forms.SmallIntegerField(
        error_messages={'required' : "수량을 입력하세요."},
        label = "수량"
    )
    d_price = forms.IntegerField(
        error_messages={'required':"도매가격을 입력하세요"},
        label = "도매가격"
    )
    memo = forms.TextField(
        error_messages={'required':" 메모를 입력하세요"},
        label = "메모"
    )
    status = forms.CharField(
        error_messages={'required':"상태를 입력하세요."},
        max_length = 30, label = "상태"
    )
    exposure = forms.CharField(
        error_messages={'required':"노출을 입력하세요."},
        max_length = 10, label = "노출"
    )

    def clean(self):
        cleaned_data = super().clean()
        jumun_id = cleaned_data.get('jumun_id')
        jumun_name = cleaned_data.get('jumun_name')
        consumer = cleaned_data.get('consumer')
        brand = cleaned_data.get('brand')
        prd_name = cleaned_data.get('prd_name')
        option = cleaned_data.get('option')
        quantity = cleaned_data.get('quantity')
        d_price = cleaned_data.get('d_price')
        memo = cleaned_data.get('memo')
        status = cleaned_data.get('status')
        exposure = cleaned_data.get('exposure')

        if not (jumun_id and jumun_name and consumer and brand and prd_name and option and quantity and d_price and memo and status and exposure):
            self.add_error('jumun_id', "값이 없습니다.")
            self.add_error('jumun_name', "값이 없습니다.")
            self.add_error('consumer', "값이 없습니다.")
            self.add_error('prd_name', "값이 없습니다.")
            self.add_error('option', "값이 없습니다.")
            self.add_error('quantity', "값이 없습니다.")
            self.add_error('d_price', "값이 없습니다.")
            self.add_error('memo', "값이 없습니다.")
            self.add_error('status', "값이 없습니다.")
            self.add_error('brand', "값이 없습니다.")
            self.add_error('exposure', "값이 없습니다.")
            
