from django import forms
from .models import Diabetic

SET_CHOICES = [
    (1, 'হা'),
    (0, 'না')
]
SET_SEX = [
    (1, 'পুরুষ'),
    (0, 'নারী')
]
class DiabeticForm(forms.ModelForm):
    HighBP = forms.ChoiceField(label = "আপনার কি উচ্চরক্তচাপ আছে?", choices=SET_CHOICES, widget=forms.RadioSelect)
    HighChol = forms.ChoiceField(label = "আপনার কি হাই কোলেস্টোরাল আছে?", choices=SET_CHOICES, widget=forms.RadioSelect)
    # CholCheck = forms.ChoiceField(label = "আপনি কি বিগত ২ বছরে কোলেস্টোরাল লেভেল চেক করিয়েছেন?", choices=SET_CHOICES, widget=forms.RadioSelect)
    Smoker = forms.ChoiceField(label = "আপনি কি ধুমপায়ী?", choices=SET_CHOICES, widget=forms.RadioSelect)
    Stroke = forms.ChoiceField(label = "আপনার কি কখনো স্ট্রোক হয়েছে?", choices=SET_CHOICES, widget=forms.RadioSelect)
    HeartDiseaseorAttack = forms.ChoiceField(label = "আপনার কি কখনো হার্ট এটাক হয়েছে বা হার্টে সমস্যা আছে?", choices=SET_CHOICES, widget=forms.RadioSelect)
    PhysActivity = forms.ChoiceField(label = "আপনি কি গত ৩০ দিনে শারীরিক ব্যায়াম বা পরিশ্রম করেছন?", choices=SET_CHOICES, widget=forms.RadioSelect)
    # Fruits = forms.ChoiceField(label = "আপনি কি নিয়মিত ফল খান?", choices=SET_CHOICES, widget=forms.RadioSelect)
    # Veggies = forms.ChoiceField(label = "আপনি কি নিয়মিত শাক-সবজি খান?", choices=SET_CHOICES, widget=forms.RadioSelect)
    HvyAlcoholConsump = forms.ChoiceField(label = "আপনি কি মদ্যপান করেন?", choices=SET_CHOICES, widget=forms.RadioSelect)
    # AnyHealthcare = forms.ChoiceField(label = "সম্প্রতি আপনি কি কোন স্বাস্থসেবা নিয়েছেন?", choices=SET_CHOICES, widget=forms.RadioSelect)
    NoDocbcCost = forms.ChoiceField(label = "গত ১২ মাসে কি এমন একটি সময় ছিল যখন আপনাকে একজন ডাক্তার দেখানোর প্রয়োজন ছিল কিন্তু খরচের কারণে পারেননি?", choices=SET_CHOICES, widget=forms.RadioSelect)
    DiffWalk = forms.ChoiceField(label = "আপনার কি হাঁটতে বা সিঁড়ি বেয়ে উঠতে গুরুতর অসুবিধা হয়?", choices=SET_CHOICES, widget=forms.RadioSelect)
    # Sex = forms.ChoiceField(label = "লিঙ্গ", choices=SET_SEX, widget=forms.RadioSelect)
    # MentHlth = forms.ChoiceField(choices=SET_DAYS, label="গত ৩০ দিনে কত দিন আপনার মানসিক স্বাস্থ্য ভালো ছিল না?", widget=forms.Select(attrs={'class': 'form-select'}))
    # PhysHlth = forms.ChoiceField(choices=SET_DAYS, label="গত ৩০ দিনে কত দিন আপনার শারিরীক স্বাস্থ্য ভালো ছিল না?", widget=forms.Select(attrs={'class': 'form-select'}))
    # GenHlth = forms.ChoiceField(choices=HEALTH_CONDITION, label="সাধারণভাবে আপনার স্বাস্থ্য হলঃ", widget=forms.Select(attrs={'class': 'form-select'}))
    # Education = forms.ChoiceField(choices=EDUCATION_LEVEL, label="আপনার শিক্ষার স্তরঃ", widget=forms.Select(attrs={'class': 'form-select'}))
    # Income = forms.ChoiceField(choices=MONTH_INCOME, label="আপনার মাসিক আয়ঃ", widget=forms.Select(attrs={'class': 'form-select'}))
    class Meta:
        model = Diabetic
        fields = ['HighBP', 'HighChol', 'Height', 'Weight', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'HvyAlcoholConsump', 'NoDocbcCost', 'GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk', 'Age', 'Education', 'Income']
        labels = {
            'Height': "আপনার দৈহিক উচ্চতা কত? (In Meter)",
            'Weight': "আপনার ওজন কত?",
            'Age': "আপনার বয়স কত বছর?",
            'Income': "আপনার মাসিক আয়ঃ",
            'GenHlth': "সাধারণভাবে আপনার স্বাস্থ্য হলোঃ", 
            'MentHlth': "গত ৩০ দিনে কত দিন আপনার মানসিক স্বাস্থ্য ভালো ছিল না?",
            'PhysHlth': "গত ৩০ দিনে কত দিন আপনার শারিরীক স্বাস্থ্য ভালো ছিল না?",
            'Education': "আপনার শিক্ষার স্তরঃ",
        }
        widgets = {
            # 'HighBP': forms.TextInput(attrs={'class': 'form-control'}), 
            # 'HighChol': forms.TextInput(attrs={'class': 'form-control'}),
            # 'CholCheck': forms.TextInput(attrs={'class': 'form-control'}),
            'Height': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "E.g. 1.8034 for 1.8034 meter"}),
            'Weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "E.g. 72.7 for 72.7 kg"}),
            # 'Smoker': forms.TextInput(attrs={'class': 'form-control'}),
            # 'Stroke': forms.TextInput(attrs={'class': 'form-control'}),
            # 'HeartDiseaseorAttack': forms.TextInput(attrs={'class': 'form-control'}), 
            # 'PhysActivity': forms.TextInput(attrs={'class': 'form-control'}),
            # 'Fruits': forms.TextInput(attrs={'class': 'form-control'}),
            # 'Veggies': forms.TextInput(attrs={'class': 'form-control'}),
            # 'HvyAlcoholConsump': forms.TextInput(attrs={'class': 'form-control'}),
            # 'AnyHealthcare': forms.TextInput(attrs={'class': 'form-control'}),
            # 'NoDocbcCost': forms.TextInput(attrs={'class': 'form-control'}),
            'GenHlth': forms.Select(attrs={'class': 'form-select'}),
            'MentHlth': forms.Select(attrs={'class': 'form-select'}),
            'PhysHlth': forms.Select(attrs={'class': 'form-select'}),
            # 'DiffWalk': forms.TextInput(attrs={'class': 'form-control'}),
            # 'Sex': forms.TextInput(attrs={'class': 'form-control'}),
            'Age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "E.g. 35 for 35 years"}),
            'Education': forms.Select(attrs={'class': 'form-select'}),
            'Income': forms.Select(attrs={'class': 'form-select'})
        }