from django.http import HttpResponse
from django.shortcuts import render
import datetime as dt
def home(request):
    isActive = True
    if request.method=='POST':
        # check = request.POST['check']
        check = request.POST.get('check')
        print(check)
        if check is None: isActive = False
        else: isActive=True

    date= dt.datetime.now()
    print("test function called from view")
    name = 'Akash Joshi'


    list_of_programs = ['WAP to check even or odd','WAP to check prime number','WAP to print pascals tringle']
    students = {'student_name':'Raghav','student_clg':'xyz','student_city':'Mumbai'}
    # return HttpResponse("<h1> Hello this is index page</h1>"+str(date))
    output = {'date':date,'name':name,'isActive':isActive,'programs':list_of_programs,'students':students}
    return render(request,"home.html",output)

def about(request):
    # return HttpResponse("<h1> this is about page</h1>")
    return render(request, "about.html", {})

def services(request):
    # return HttpResponse("<h1> this is service page</h1>")
    return render(request, "services.html", {})