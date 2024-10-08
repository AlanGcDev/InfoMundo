from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Construir el cuerpo del correo
            email_body = f"Nombre: {name}\nEmail: {email}\n\nMensaje:\n{message}"
            
            # Enviar correo electrónico
            send_mail(
                subject=f"Nuevo mensaje de contacto: {subject}",
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['infomundo.web@gmail.com'],
                fail_silently=False,
            )
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contacto.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')
# Create your views here.
def index(request):
    return render(request, 'index.html')

def juegos(request):
    return render(request, 'juegos.html')

def noticias(request):
    return render(request, 'noticias.html')

def deportes(request):
    return render(request, 'deportes.html')

def terminos(request):
    return render(request, 'terminos.html')

def uso_content(request):
    return render(request, 'uso_content.html')

def nosotros(request):
    return render(request, 'nosotros.html')
