from django.db import models
from django.core.exceptions import ValidationError
import os

# Define a pasta para armazenar o arquivo de upload
def path_upload(instance,filename):
    # Obtém o número total de uploads existentes
    total_uploads = Pdi.objects.count()
    
    # Gera o nome da pasta com base no número de uploads
    subfolder = f'upload{total_uploads + 1}'
    
    # Concatena o caminho completo do arquivo
    return os.path.join('uploads', subfolder, filename)


class Pdi(models.Model):
    objective_title = models.CharField('Titulo do Objetivo',max_length = 25, null = False, blank = False)
    developed_areas = models.CharField('Áreas ',max_length = 100, null = False, blank = False)
    initial_datetime = models.DateTimeField('Data Inicio')
    final_datetime = models.DateTimeField('Data Final')
    reference_url = models.URLField('Link de Referência')
    file = models.FileField('Arquivo',upload_to=path_upload, blank=True, null=True)
    description = models.TextField('Descrição')
    
    
    def clean(self):
        # Verifica se a data final é anterior à data inicial
        if self.final_datetime and self.initial_datetime:
            if self.final_datetime < self.initial_datetime:
                raise ValidationError('Data final deve ter seu prazo posterior à data inicial.')