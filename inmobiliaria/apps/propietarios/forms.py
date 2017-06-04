from django import forms
from apps.propietarios.models import Propietario

class PropietarioForm(forms.ModelForm):

	class Meta:
		model = Propietario

		fields = [
			'nombre',
			'apellidos',
			'fecha_nacimiento',
			'direccion',
			'telefono',
			'email',
		]
		labels = {
			'nombre': 'Nombre',
			'apellidos': 'Apellidos',
			'fecha_nacimiento': 'Fecha de nacimiento',
			'direccion': 'Direccion',
			'telefono': 'Telefono',
			'email': 'Email',
		}
		widgets ={
			'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Introduce tu nombre'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control','placeholder':'Introduce tu apellido/s'}),
			'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control','placeholder':'Fecha de nacimiento en formato dd/mm/YYYY'}),
			'direccion': forms.TextInput(attrs={'class':'form-control','placeholder':'Introduce la direccion de tu vivienda actual'}),
			'telefono': forms.TextInput(attrs={'class':'form-control','placeholder':'numero de telefono (con prefijo si es necesario)'}),
			'email': forms.TextInput(attrs={'class':'form-control','placeholder':'direccion de correo electronico'}),
		}