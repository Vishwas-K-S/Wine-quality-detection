from django.shortcuts import render
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pickle

def home(request):
    return render(request, 'wine.html')


def getPrediction(fixed_acidity, volatile_acidity, citric_acid, residual_sugar,chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,pH, sulphates, alcohol):
    model = pickle.load(open('source/rfc.sav','rb'))
    prediction = model.predict([
        [fixed_acidity, volatile_acidity, citric_acid, residual_sugar,chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,pH, sulphates, alcohol]
    ])
    return prediction

def result(request):
    fixed_acidity = float(request.POST.get('fixed_acidity', False))
    volatile_acidity = float(request.POST.get('volatile_acidity', False))
    citric_acid = float(request.POST.get('citric_acid', False))
    residual_sugar = float(request.POST.get('residual_sugar', False))
    chlorides = float(request.POST.get('chlorides', False))
    free_sulfur_dioxide = float(request.POST.get('free_sulfur_dioxide', False))
    total_sulfur_dioxide = float(request.POST.get('total_sulfur_dioxide', False))
    density = float(request.POST.get('density', False))
    pH = float(request.POST.get('pH', False))
    sulphates = float(request.POST.get('sulphates', False))
    alcohol = float(request.POST.get('alcohol', False))
    
    res = getPrediction(fixed_acidity, volatile_acidity, citric_acid, residual_sugar,chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,pH, sulphates, alcohol)
    if res[0] == 1:
        return render(request, 'wine.html', {'res':'Bad'})
    elif res[0] == 2:
        return render(request, 'wine.html', {'res':'Average'})
    else:
        return render(request, 'wine.html', {'res':'Good'})

    