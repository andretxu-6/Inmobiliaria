from django import forms
from apps.inmuebles.models import Inmueble

class InmuebleForm(forms.ModelForm):

	class Meta:
		model = Inmueble

		fields = [
			'direccion',
			'metros',
			'precio',
			'habitaciones',
			'descripccion',
			'opcion',
			'disponibilidad',
			'ciudad',
			'propietario',
		]
		labels = {
			'direccion': 'Direccion',
			'metros': 'Metros cuadrados',
			'precio': 'Precio',
			'habitaciones': 'Habitaciones',
			'descripccion': 'Descripcion',
			'opcion': 'Alquiler o venta',
			'disponibilidad': 'Disponibilidad',
			'ciudad': 'Ciudad',
			'propietario': 'Propietario',
		}
		widgets ={
			'direccion': forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion del apartamento'}),
			'metros': forms.TextInput(attrs={'class':'form-control','placeholder':'Numero de metros cuadrados'}),
			'precio': forms.TextInput(attrs={'class':'form-control','placeholder':'Precio de la vivienda'}),
			'habitaciones': forms.TextInput(attrs={'class':'form-control','placeholder':'Numero de habitaciones'}),
			'descripccion': forms.TextInput(attrs={'class':'form-control','placeholder':'Descripccion del inmueble'}),
			'opcion': forms.TextInput(attrs={'class':'form-control','placeholder':'introduce \"v\" para venta y \"a\" para alquiler'}),
			'disponibilidad': forms.CheckboxInput(attrs={'class':'form-control'}),
			'ciudad': forms.Select(attrs={'class':'form-control'}),
			'propietario': forms.Select(attrs={'class':'form-control'}),
		}