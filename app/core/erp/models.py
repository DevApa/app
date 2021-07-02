from django.db import models
from datetime import datetime

from core.erp.choices import gender_choices


class Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Employee(models.Model):
    categ = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=20)
    dni = models.CharField(max_length=10, unique=True)
    date_joined = models.DateField(default=datetime.now)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']


class Product(models.Model):
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    file = models.FileField(upload_to='path/%Y/%m/%d', max_length=100, blank=True, null=True)
    pvp = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de Nacimiento')
    address = models.CharField(max_length=150, null=True,blank=True)
    sex = models.CharField(max_length=10, choices=gender_choices, default='Femenino', verbose_name='Sexo')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural='Clientes'
        ordering = ['id']


class Sale(models.Model):
    client = models.ForeignKey(Client, null=False, blank=False, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(max_digits=9, decimal_places=2)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    iva = models.DecimalField(max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.client.names

    class Meta:
        ordering = ['id']
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.PositiveIntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'name'
        verbose_name_plural = 'Detalle Venta'
