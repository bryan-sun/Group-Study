from django.http import HttpResponse

from django.template import RequestContext, loader

from .models import *
from django.template import Context, Template
from . import authentication
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import get_object_or_404, render, render_to_response

def index(request):

    #buildings = Places.objects.all()

    template = loader.get_template('study/SignIn.html')

    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))






def inbuilding(request,build_id):

    checked = checkedIn.objects.filter(atBuilding = build_id)

    template = loader.get_template('study/selected.html')

    context = RequestContext(request, {

        'checked':checked,

    })
    return HttpResponse(template.render(context))

def openUser(request,build_id,student_id):

    classes = studentClasses.objects.filter(student = student_id)

    student = Student.objects.filter(id = student_id)

    current = Current.objects.filter(user = student_id)


    template = loader.get_template('study/viewUser.html')

    context = RequestContext(request, {
        'student':student,
        'class':classes,
        'cur':current,

    })
    return HttpResponse(template.render(context))

def signIn(request):

    context = RequestContext(request)

    user_id = request.POST['netID']
    user_pass = request.POST['password']

    check = authentication.login(user_id,user_pass)

    if not user_id or not user_pass:
         context = RequestContext(request, {
            'warning':'Error: the field are empty bruh'

          })
         template = loader.get_template('study/SignIn.html')

         return HttpResponse(template.render(context))


    elif (check == "0"):
         buildings = Places.objects.all()

         template = loader.get_template('study/test.html')

         context = RequestContext(request, {
            'build':buildings

          })
         return HttpResponse(template.render(context))

    elif (check == "-1"):
         context = RequestContext(request, {
            'warning':'Error: you spelled your netid/password wrong you pleb'

          })
         template = loader.get_template('study/SignIn.html')

         return HttpResponse(template.render(context))

    elif (check == "-2"):
         context = RequestContext(request, {
            'warning':'Error: something is weird. please annoy the univeristy not us'

          })
         template = loader.get_template('study/SignIn.html')

         return HttpResponse(template.render(context))

    else:
        template = loader.get_template('study/SignIn.html')

        return HttpResponse(template.render(context))
