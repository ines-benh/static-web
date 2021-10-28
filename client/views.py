from django.shortcuts import render
from client.forms import ClientModelform

# Create your views here.



def client(request):
    form = ClientModelform(request.POST)

    if request.method == "POST":
       
        form.save()
        form = ClientModelform()
    else:
        form = ClientModelform() 


    context = {

            'form' : form

    }
    return render(request,"client/index.html",context)