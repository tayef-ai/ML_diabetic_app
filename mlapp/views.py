from django.shortcuts import render
from .forms import DiabeticForm
from django.http import HttpResponseRedirect
from joblib import load
from .models import Diabetic
from django.contrib import messages
from django.contrib.auth.decorators import login_required

scalar = load('scalar.joblib') 
clf_from_joblib = load('model.joblib') 
@login_required()
def mlviews(request):
    if request.method == 'POST':
        form = DiabeticForm(request.POST)
        if form.is_valid():
            hb = form.cleaned_data['HighBP']                
            hc = form.cleaned_data['HighChol']              
            ht = form.cleaned_data['Height']   
            wt = form.cleaned_data['Weight']               
            smoke = form.cleaned_data['Smoker']               
            stk = form.cleaned_data['Stroke']               
            hda = form.cleaned_data['HeartDiseaseorAttack'] 
            pa = form.cleaned_data['PhysActivity']         
            hac = form.cleaned_data['HvyAlcoholConsump']    
            ndc = form.cleaned_data['NoDocbcCost']          
            gh = form.cleaned_data['GenHlth']              
            mh = form.cleaned_data['MentHlth']             
            ph = form.cleaned_data['PhysHlth']             
            dw = form.cleaned_data['DiffWalk']             
            ag = int(form.cleaned_data['Age'])                  
            edu = form.cleaned_data['Education']            
            inc = form.cleaned_data['Income'] 
            bmi = int(wt/(ht*ht))
            X_test = scalar.transform([[hb, hc, bmi, smoke, stk, hda, pa, hac, ndc, gh, mh, ph, dw, ag, edu, inc]])
            db = clf_from_joblib.predict(X_test)    
            reg = Diabetic(HighBP=hb, HighChol=hc, Height=ht, Weight=wt, Smoker=smoke, Stroke=stk, HeartDiseaseorAttack=hda, PhysActivity=pa, HvyAlcoholConsump=hac, NoDocbcCost=ndc, GenHlth=gh, MentHlth=mh, PhysHlth=ph, DiffWalk=dw, Age=ag, Education=edu, Income=inc, Diabetes_binary=db[0])
            reg.save()
            form = DiabeticForm()
            if(db[0]==1):
                messages.warning(request, "আপনি উচ্চ ডায়বেটিস ঝুকিতে আছেন!!!")
            else: 
                messages.success(request, "আপনি ডায়বেটিস ঝুঁকিমুক্ত।")
            HttpResponseRedirect('/')
    else:
        form = DiabeticForm()
    return render(request, 'home.html', {'form_context': form})


