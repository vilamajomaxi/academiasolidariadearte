from django import forms
from alumnos.models import *

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=50, widget=forms.TextInput(
            attrs={'placeholder': 'Ingrese su usuario', 'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(
            attrs={'placeholder': 'Ingrese su password', 'class': 'form-control'}))


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['sede','nombre','apellido','direccion','barrio','ciudad','fecha_nacimiento','telefono','telefonoFijo','email']


    def __init__(self, *args, **kwargs):
        super(AlumnoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})



date_choices = (
            ('0', "enero"),
            ('1',	"febrero"),
            ('2',	"marzo"),
            ('3',	"abril"),
            ('4',	"mayo"),
            ('5',	"junio"),
            ('6',	"julio"),
            ('7',	"agosto"),
            ('8',	"septiembre"),
            ('9',	"octubre"),
            ('10',"noviembre"),
            ('11',	"diciembre"),
)

class Filterform(forms.Form):
    mes = forms.ChoiceField(label = "Mes",choices = date_choices,required=False)
    sede = forms.ChoiceField(label = "Sede",choices= sede_choices ,required=False)


    def __init__(self, *args, **kwargs):
        super(Filterform, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})

