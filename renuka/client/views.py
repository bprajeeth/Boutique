from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from client.models import client
# Create your views here.

def home_view(request):
    return render(request,"Home.html")

def form_view(request):
    if request.method == 'POST':
        print(request.POST)
# VALUE INSIDE BRACKETS ARE ID FROM HTML TAGS
        username = request.POST['name']
        mob = request.POST['mobile']
        dress = request.POST['dress']

        shoulder = request.POST['shoulder']
        bust1 = request.POST['bust1']
        bust2 = request.POST['bust2']
        bust3 = request.POST['bust3']
        blouse = request.POST['blouse']
        arm1 = request.POST['arm1']
        arm2 = request.POST['arm2']
        arm3 = request.POST['arm3']
        wst = request.POST['waist']
        saree1 = request.POST['saree1']
        saree2 = request.POST['saree2']
        knee = request.POST['knee']
        thav = request.POST['thavani']
        pyjama1 = request.POST['pyjama1']
        pyjama2 = request.POST['pyjama2']
        pyjama3 = request.POST['pyjama3']
        pyjama4 = request.POST['pyjama4']


        user = client(name=username, mobile=mob, dress_type=dress, shoulder_to_shoulder=shoulder, above_bust=bust1, top_bust=bust2 ,below_bust=bust3 , blouse_length=blouse , arm_hole=arm1, arm_width=arm2,  arm_length=arm3, waist=wst , saree_length=saree1, saree_waist=saree2, knee_to_knee=knee , thavani=thav, pyjama_waist=pyjama1, pyjama_hip=pyjama2, pyjama_length=pyjama3, pyjama_ankle=pyjama4)
        #user = client(shoulder_to_shoulder=shoulder, above_bust=bust1, top_bust=bust2 ,below_bust=bust3 , blouse_length=blouse , arm_hole=arm1, arm_width=arm2,  arm_length=arm3, waist=wst , saree_length=saree1, saree_waist=saree2, knee_to_knee=knee , thavani=thav, pyjama_waist=pyjama1, pyjama_hip=pyjama2, pyjama_length=pyjama3, pyjama_ankle=pyjama4)
        user.save()  
        return HttpResponse("successfull")       

    else:
        return render(request, "form.html")     

def costumes_view(request):
    return render(request,"Patterns.html")
    #return HttpResponse("Patterns.html")

def ornaments_view(request):
    return render(request,"Jewellery.html")

def accessories_view(request):
    return render(request,"Accessories.html")





    