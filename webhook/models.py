from django.db import models


class WebhookRequest(models.Model):
    data = models.JSONField()
