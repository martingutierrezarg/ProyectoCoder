from django.shortcuts import  render, redirect
from .forms import AuthenticationForm, NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UpdateUserForm, UpdateProfileForm



def register_request(request):
	title = "Registration"
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registro exitoso." )
			return redirect("products:product_list")
		messages.error(request, "Registro fallido. Información inválida.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form, 'title': title})


def login_request(request):
	title = "Login"
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=email, password=password)
			if user is not None:
				login(request, user)
				return redirect("products:product_list")
			else: 
				messages.error(request, "products:product_list")
		else:
			messages.error(request, 'usuario o contraseña invalido')
	form = AuthenticationForm()
	return render(request=request, template_name='login.html', context={'login_form': form, 'title': title})

@login_required
def logout_request(request):
	logout(request)
	messages.info(request, "Has terminado tu sesion satisfactoriamente")
	return redirect("products:product_list")

@login_required
def profile_request(request):
	title = "Profile"
	return render(request=request, template_name='profile.html', context={'title': title})

@login_required
def edit_profile(request):
	title = "Edit Profile"
	if request.method == 'POST':
		user_form = UpdateUserForm(request.POST, instance=request.user)
		profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Su perfil se actualizo con exito')
	else:
		user_form = UpdateUserForm(instance=request.user)
		profile_form = UpdateProfileForm(instance=request.user.profile)

	return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form' : profile_form, 'title': title})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Cambio de contraseña exitoso"
    success_url = reverse_lazy('accounts:edit_profile')
    

class PasswordResetView(SuccessMessageMixin, PasswordResetView):
	template_name = 'reset_password.html'
	email_template_name = 'reset_password_email.html'
	success_message = "Le hemos enviado instrucciones por correo electrónico para establecer su contraseña, " \
                      "si existe una cuenta con el correo electrónico que ingresó. Deberías recibirlos en breve." \
                      " Si no recibe un correo electrónico, " \
                      "asegúrese de haber ingresado la dirección con la que se registró y verifique su carpeta de correo no deseado."
	success_url = reverse_lazy('products:product_list')