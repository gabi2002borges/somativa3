from django.db import models


class Medico(models.Model):
    nome = models.CharField(max_length=20, default=None)
    crm = models.CharField(max_length=15)
    especialidade = models.CharField(max_length=60, default=None)
    foto = models.ImageField(blank=True, upload_to='foto_produto/%y/%m/%d/')
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    data = models.DateField(auto_now=False, auto_now_add=False, default=None)
    TIME_CHOICE = (
    ( '9 AM', '09:00:00'),
    ('10 AM', '10:00:00'),
    ('11 AM', '11:00:00'),
    ('12 PM', '12:00:00'),
    ('1 PM', '13:00:00'),
    ('2 PM', '14:00:00'),
    ('3 PM', '15:00:00'),
    )
    horario = models.CharField(max_length=10, choices=TIME_CHOICE)
    medicos = models.ForeignKey(Medico, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.data, self.horario, self.medicos.nome



