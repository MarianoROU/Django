from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Home(request):
    return render(request, 'index.html')

def Usuario_Registro(request):
    return render(request, 'usuario_registro.html')


def Empleo_Registro(request):
    return render(request, 'empleo_registro.html')

def Empresa_Registro(request):
    return render(request, 'empresa_registro.html')

def Empleo_Listado(request):
    return render(request, 'empleo_listado.html')

def Calcular_Sueldo(request):

    if request.GET['nominal']:

        nominal = int(request.GET['nominal'])
        horas_extras = int(request.GET['extras'])

        valor_hora = round((nominal / 30) / 8, 2)

        if horas_extras > 1:

            nominal_mas_extras = (valor_hora * horas_extras) + nominal

            mensaje=  str(nominal_mas_extras)
        else:
            if horas_extras < 1:

                mensaje = nominal

            else:

                nominal_mas_extras = valor_hora + nominal
                mensaje = nominal_mas_extras

    else:

        mensaje = 'algo anda mal'
    return HttpResponse(mensaje)