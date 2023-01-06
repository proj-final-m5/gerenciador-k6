from django.http import HttpResponse
from django.core.mail import send_mail


def send_invite(assunto, schedule, link, email):
    send_mail(
        # Campos do email
        assunto,
        # Msg padrão do convite para a task
        f"{schedule}\n Clique no link abaixo para aceitar o convite: \n {link}",
        # Email de quem irá enviar
        "equipe_k6@outlook.com",
        # Lista de emails que irão receber o convite
        [email],
    )
