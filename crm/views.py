from django.shortcuts import render,redirect

from crm.forms import StudentCreateForm
from django.views.generic import View
from crm.models import Students

class StudentCreateView(View):

    def get(self,request,*args,**kwargs):
        form=StudentCreateForm()
        return render(request,"student_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("stud-list")
        else:
            return render(request,"student_add.html",{"form":form})


class StudentListView(View):
    def get(self,request,*args,**kwargs):
        qs=Students.objects.all()
        return render(request,"student_list.html",{"students":qs})



class StudentDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Students.objects.get(id=id)
        return render(request,"student_detail.html",{"student":qs})
    

class SytudentUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Students.objects.get(id=id)
        form=StudentCreateForm(instance=obj)
        return render(request,"student_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Students.objects.get(id=id)
        form=StudentCreateForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("stud-list")
        else:
            return render(request,"student_edit.html",{"form":form})

        
class StudentDeleteView(View):
    def get(self,request,*args,**kwrags):
        id=kwrags.get("pk")
        Students.objects.filter(id=id).delete()
        return redirect("stud-list")
    


    