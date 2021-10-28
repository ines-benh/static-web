from django.shortcuts import render
from contact.forms import ContactModelform


def contact(request):
    form = ContactModelform(request.POST)

    if request.method == "POST":
       
        form.save()
        form = ContactModelform()
    else:
        form = ContactModelform() 


    context = {

            'form' : form

    }
    return render(request,"contact/index.html",context)

