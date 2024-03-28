from django import forms
from .models import Student

#creer class pour formulaire ajout

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student   #specifier le modele
        #fields = '__all__'
        fields =['matricule',
                'prenom',
                'nom', 
                'email', 
                'domaine_etude', 
                'gpa']

        #personaliser les labels
        labels = {
            'matricule': 'Matricule',
            'prenom':'Prenom',
            'nom': 'Nom',
            'email':'Email',
            'domaine_etude':'Domaine d\'étude',
            'gpa':'GPA'
        }

        #personaliser les fields inputs avec bootstrap
        widgets ={
         'matricule': forms.NumberInput(attrs={'class':'forms-control'}),
            'prenom':forms.TextInput(attrs={'class':'forms-control'}),
            'nom': forms.TextInput(attrs={'class':'forms-control'}),
            'email':forms.EmailInput(attrs={'class':'forms-control'}),
            'domaine_etude':forms.TextInput(attrs={'class':'forms-control'}),
            'gpa':forms.NumberInput(attrs={'class':'forms-control'})

        }