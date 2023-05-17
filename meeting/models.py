from django.db import models

class Meeting(models.Model):
    title = models.CharField('Titulo',max_length = 25, null = False, blank = False)
    collaborator = models.CharField('Colaborador', max_length = 25, null =False, blank = False)
    datetime = models.DateTimeField('Data e Hora')
    details = models.TextField('Detalhes')
    url_meeting = models.URLField()

    def __str__(self):
        return self.title
        