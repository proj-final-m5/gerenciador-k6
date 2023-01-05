from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

def invite(request):
    send_mail(
        # Campos do email
        'Assunto', 
        # Msg padrão do convite para a task
        'Gerenciamento K6', 
        # Email de quem irá enviar
        'carolinapezzin@outlook.com',
        # Lista de emails que irão receber o convite
        ['cakakau@gmail.com','carolinapezzinferreira@gmail.com'], 
        )
    return HttpResponse('Email enviado com sucesso')
