from django.shortcuts import render , HttpResponse
from home.forms.feedback import feedback
from home.models import Feedback


# Create your views here.
def index(request):
    return render(request , template_name='home/index.html')
   
def about_us(request):
    return render(request , template_name='home/about_us.html')


def skill(request):
    return render(request , template_name='home/skill.html')


def contact_us(request):
    if request.method == 'GET':
       #get request
        form= feedback()
        
      
        return render(request ,'home/contact_us.html' ,{"form" : form })
    else:
        #post request

        form =feedback(request.POST)
     
       

        if form.is_valid():

            name = form.cleaned_data.get('name')
            email=form.cleaned_data.get('email')
            comment=form.cleaned_data.get('comment')

            contact=Feedback()
            contact.name=name
            contact.email=email
            contact.comment=comment
            contact.save()
            
           
               



def project(request):
    return render(request , template_name='home/project.html')    


    
