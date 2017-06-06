from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#coger la clase de usuarios ya creada y anadir atributos que ya estan en la tabla auth_user
class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]
		labels = {
			'username': 'Nombre de usuario',
			'fist_name': 'Nombre',
			'last_name': 'Apellidos',
			'email': 'Email',
		}