from django.db import models


class TimeCourseChoices(models.TextChoices):
    AM = "AM"
    PM = "PM"


class PriorityChoices(models.TextChoices):
    baixa = "Baixa"
    media = "Média"
    alta = "Alta"


class CategoryChoices(models.TextChoices):
    lazer = "Lazer"
    trabalho = "Trabalho"
    reuniao = "Reunião"
    familia = "Família"
    projetos = "Projetos"
    esportes = "Esportes"
    tarefas = "Tarefas"
    saude = "Saúde"
    festas = "Festas"


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=127)
    time_course = models.CharField(
        max_length=20, choices=TimeCourseChoices.choices)
    schedule_time = models.CharField(max_length=20)
    schedule_date = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    priority = models.CharField(
        max_length=20, choices=PriorityChoices.choices, default=PriorityChoices.baixa
    )
    guests = models.CharField(max_length=500)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="tasks"
    )
    category = models.CharField(
        max_length=20, choices=CategoryChoices.choices, default=CategoryChoices.tarefas
    )
