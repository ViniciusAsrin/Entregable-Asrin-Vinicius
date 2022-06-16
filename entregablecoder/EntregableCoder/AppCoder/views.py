from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Familiares
from django.template import Template, Context



def plantilla1(self):
    familiar1 = Familiares(nombre = "Agustin", edad = "19", fecha_nac = "2003-01-29")
    familiar1.save()

    diccionario = {"Nombre":familiar1.nombre, "Edad":familiar1.edad, "Fecha_de_Nacimiento":familiar1.fecha_nac}

    miHtml = open("C:/Users/Vinit/OneDrive/Escritorio/entregablecoder/EntregableCoder/EntregableCoder/plantillas/template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context(diccionario)

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)



def plantilla2(self):
    familiar2 = Familiares(nombre = "Ana", edad = "2", fecha_nac = "2000-03-15")
    familiar2.save()

    diccionario = {"Nombre":familiar2.nombre, "Edad":familiar2.edad, "Fecha_de_Nacimiento":familiar2.fecha_nac}

    miHtml = open("C:/Users/Vinit/OneDrive/Escritorio/entregablecoder/EntregableCoder/EntregableCoder/plantillas/template2.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context(diccionario)

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)    




def plantilla3(self):
    familiar3 = Familiares(nombre = "Mariano", edad = "12", fecha_nac = "2010-02-24")
    familiar3.save()

    diccionario = {"Nombre":familiar3.nombre, "Edad":familiar3.edad, "Fecha_de_Nacimiento":familiar3.fecha_nac}

    miHtml = open("C:/Users/Vinit/OneDrive/Escritorio/entregablecoder/EntregableCoder/EntregableCoder/plantillas/template3.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context(diccionario)

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)          

# Create your views here.
