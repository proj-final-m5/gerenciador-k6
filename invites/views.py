from django.http import HttpResponse
from django.core.mail import send_mail


def invite(request, assunto, link, *args):
    send_mail(
        # Campos do email
        assunto,
        # Msg padrão do convite para a task
        "Clique no link abaixo para aceitar o convite" + link,
        # Email de quem irá enviar
        "equipe_k6@outlook.com",
        # Lista de emails que irão receber o convite
        [args],
    )
    return HttpResponse("Email enviado com sucesso")
