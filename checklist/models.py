from django.db import models
import json

class Checklist(models.Model):
    title = models.CharField(max_length=250)
    campos_dinamicos = models.TextField(blank=True, null=True)

    def save_campos_dinamicos(self, campos):
        self.campos_dinamicos = json.dumps(campos)

    def get_campos_dinamicos(self):
        return json.loads(self.campos_dinamicos) if self.campos_dinamicos else []
