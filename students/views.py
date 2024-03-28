from django.shortcuts import render
from .models import Student
#pour views students
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import StudentForm 
# Create your views here.
def index(request):
    return render(request, 'students/index.html', {
        'students':Student.objects.all()
    })

def view_student(request,id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        #verifier si les infos sont valides
        if form.is_valid():
            #recuperons les donnees valides nettoyer
            new_std_matriule =form.cleaned_data['matricule']
            new_std_prenom =form.cleaned_data['prenom']
            new_std_nom =form.cleaned_data['nom']
            new_std_email =form.cleaned_data['email']
            new_std_domaine =form.cleaned_data['domaine_etude']
            new_std_gpa =form.cleaned_data['gpa']

            # add un new student
            new_student= Student(
                matricule=new_std_matriule,
                prenom=new_std_prenom,
                nom=new_std_nom,
                email =new_std_email,
                domaine_etude =new_std_domaine,
                gpa=new_std_gpa
            )
            # save student
            new_student.save()
            #on redirige vers la vue success
            return render(request,'students/add.html',{
                'form':form,
                'success':True

            })
    else:
        #on retourne encore le formulaire
        form = StudentForm()
        return render(request,'students/add.html',{
            'form':form
        })