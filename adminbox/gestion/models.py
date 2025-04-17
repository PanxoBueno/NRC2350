from django.db import models
from django.contrib.auth.models import User

class Entrenador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.especialidad}"

class Atleta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.get_full_name()

class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    horario = models.DateTimeField()
    capacidad = models.IntegerField()
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.horario}"

class Reserva(models.Model):
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('atleta', 'clase')  # Evita reservas duplicadas