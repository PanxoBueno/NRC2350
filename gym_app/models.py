from django.db import models


class Categoria(models.Model):
    Categoria_esp =(
        ('halterofilia', 'Halterofilia'),
        ('gimnasio', 'Gimnasio'),
        ('metcon', 'Metcon'),
        ('crossfit', 'CrossFit'),
    )
    Planes = [
    [0, "8 Clases"],
    [1, "12 Clases"],
    [2, "16 Clases"],
    [3, "Open Box"],
    [4, "Full Clases"]
    ]

class Atleta(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    plan = models.IntegerField(choices=Categoria.Planes)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Entrenador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=20, choices=Categoria.Categoria_esp)

    def __str__(self):
        return self.nombre

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to="ejercicios", null=True)

    def __str__(self):
        return self.nombre
    
#aca agrego funcionalidad de reservas
class Clase(models.Model):
    HORARIOS = [
        ('06:00', '06:00 AM'),
        ('07:00', '07:00 AM'),
        ('08:00', '08:00 AM'),
        ('17:00', '05:00 PM'),
        ('18:00', '06:00 PM'),
        ('19:00', '07:00 PM'),
    ]
    
    nombre = models.CharField(max_length=50)
    horario = models.CharField(max_length=5, choices=HORARIOS)
    fecha = models.DateField()
    entrenador = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True)
    capacidad_maxima = models.PositiveIntegerField(default=15)
    
    def __str__(self):
        return f"{self.nombre} - {self.get_horario_display()} - {self.fecha}"

class Reserva(models.Model):
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('atleta', 'clase')  # Evita reservas duplicadas
    
    def __str__(self):
        return f"{self.atleta} - {self.clase}"