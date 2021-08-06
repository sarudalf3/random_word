from django.shortcuts import render, redirect

def redirect(request):
    # esta es la ruta de éxito
    return redirect("form/")

def index(request):
    return render(request,"form/index.html")

def create_user(request):
    print("Got Post Info....................")
    #print(request.POST)
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    print(name_from_form)
    print(email_from_form)
    context = {
        "name_on_template" : name_from_form,
        "email_on_template" : email_from_form
    }    
    return redirect("form/success")

def success(request):
    # esta es la ruta de éxito
    return render(request,"success.html")

