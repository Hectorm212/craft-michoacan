from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Perfil

def Registro(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        nombre = request.POST.get('nombre')
        domicilio = request.POST.get('domicilio')
        ciudad = request.POST.get('ciudad')
        cp = request.POST.get('cp')

        if User.objects.filter(username=email).exists():
            messages.error(request, 'El correo electrónico ya está registrado.')
            return redirect('Registro')

        user = User.objects.create_user(username=email, email=email, password=password)
        Perfil.objects.create(
            usuario=user,
            nombre_completo=nombre,
            domicilio=domicilio,
            ciudad=ciudad,
            cp=cp
        )
        messages.success(request, 'Cuenta creada exitosamente. Inicia sesión.')
        return redirect('Login')

    return render(request, 'artesanias/registro.html')

def Login(request):
    if request.method == 'POST':
        identificador = request.POST.get('username') or request.POST.get('email')
        password = request.POST.get('password')
        
        # 1. Intentar autenticar con el identificador ingresado
        user = authenticate(request, username=identificador, password=password)

        # 2. Si falló y parece correo, buscar por campo email
        if user is None and '@' in identificador:
            try:
                usuario_obj = User.objects.get(email=identificador)
                user = authenticate(request, username=usuario_obj.username, password=password)
            except User.DoesNotExist:
                user = None

        # 3. Validaciones de acceso
        if user is not None:
            # Bloquear cuentas de administrador o staff en la tienda pública
            if user.is_superuser or user.is_staff:
                messages.error(request, 'Las cuentas administrativas deben acceder exclusivamente desde el panel /admin.')
                return redirect('Login')

            login(request, user)
            return redirect('Principal')
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')
            return redirect('Login')

    return render(request, 'artesanias/login.html')

def Logout(request):
    logout(request)
    return redirect('Principal')