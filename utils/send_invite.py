import os

import dotenv
from django.core.mail import send_mail
from rest_framework import serializers

from contacts.models import Contact
from invites.models import Invite
from users.models import User

dotenv.load_dotenv()


def send_invite(assunto, schedule, link, email):
    send_mail(
        # Campos do email
        assunto,
        # Msg padrão do convite para a task
        f"{schedule}\n Clique no link abaixo para aceitar o convite: \n {link}",
        # Email de quem irá enviar
        os.getenv("EMAIL_HOST_USER"),
        # Lista de emails que irão receber o convite
        [email],
    )


def check_email(email_list, user_id):
    for email in email_list:
        contacts = list(Contact.objects.filter(
            user_id=user_id, email=email))

        if not contacts:
            raise serializers.ValidationError(
                {"detail": f"Email {email} not found in contacts"})


def send_invite_from_list(email_list, task_obj, user_obj):
    for email in email_list:
        try:
            contacts = list(Contact.objects.filter(
                user_id=user_obj.id, email=email))

            invite_obj = Invite.objects.create(
                contact=contacts[0], task=task_obj)
            invite_obj.save()

            assunto = task_obj.category
            user = User.objects.get(pk=user_obj.id)
            schedule = f"Olá, o usuário {user.username}, agendou a {task_obj.name}, no dia {task_obj.schedule_date} às {task_obj.schedule_time}"
            link = f"http://127.0.0.1:8000/api/user/invite/{invite_obj.id}/"
            send_invite(assunto, schedule, link, email)
        except Exception:
            raise serializers.ValidationError(
                {"detail": f"Error sending email to {email}"})
