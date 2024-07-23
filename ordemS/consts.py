from django.db.models import TextChoices


class StatusOs(TextChoices):
    OPEN = "open", "Aberta"
    IN_PROGRESS = "in_progress", "Em andamento"
    COMPLETED = "completed", "Concluída"
    CANCELED = "canceled", "Cancelada"
