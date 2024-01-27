from django.db import models
from unixtimestampfield.fields import UnixTimeStampField


class Person(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=True)
    employment_date = UnixTimeStampField(use_numeric=True)
    email = models.CharField(max_length=100, null=True)
    position = models.ForeignKey(
        'Position',
        on_delete=models.CASCADE,
        verbose_name='Должность'
    )
    salary = models.ForeignKey(
        'Salary',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Оклад'
    )
    department = models.ForeignKey(
        'Department',
        on_delete=models.CASCADE,
        null=False,
        verbose_name='Структурное подразделение'
    )
    project = models.ManyToManyField(
        'Project',
        related_name='person',
        null=True,
        verbose_name='Проект на который назначен'
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = "Сотрудники"


class Position(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Название должности'
    )

    class Meta:
        verbose_name = 'Должность'


class Department(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Название подразделения'
    )
    type = models.ForeignKey(
        'DepartmentType',
        on_delete=models.CASCADE,
        null=False,
        verbose_name='Тип подразделения'
    )
    address = models.ForeignKey(
        'Address',
        on_delete=models.CASCADE,
        null=False,
        verbose_name='Адрес филиала'
    )

    class Meta:
        verbose_name = 'Структурное подразделение'


class Address(models.Model):
    name = models.CharField(
        max_length=550,
        null=False
    )

    class Meta:
        verbose_name = 'Адрес'


class DepartmentType(models.Model):
    name = models.CharField(
        max_length=30,
        null=False
    )

    class Meta:
        verbose_name = 'Тип структурного подразделения'


class Project(models.Model):
    name = models.CharField(
        max_length=30,
        null=False
    )

    class Meta:
        verbose_name = 'Проект'


class Salary(models.Model):
    value = models.PositiveSmallIntegerField(default=0)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        null=False
    )
    position = models.ForeignKey(
        'Position',
        on_delete=models.CASCADE,
        null=False
    )

    class Meta:
        verbose_name = 'Оклад'
        constraints = [
            models.UniqueConstraint(
                name='unique_booking_d_f',
                fields=['value',
                        'project',
                        'position']
            )
        ]
