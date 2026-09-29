from django.db import models


class Department(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=150, verbose_name="Назва")
    head_of_department = models.CharField(max_length=120, verbose_name="Завідувач кафедри")

    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(max_length=150, verbose_name="Назва дисципліни")

    def __str__(self):
        return self.name


class Specialty(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=150, verbose_name="Назва")
    code = models.CharField(max_length=20, verbose_name="Код")
    description = models.TextField(verbose_name="Опис")
    coordinator_name = models.CharField(max_length=120, verbose_name="Імʼя координатора набору")
    coordinator_contact = models.CharField(max_length=120, verbose_name="Контакт координатора")

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='specialties',
        verbose_name="Випускова кафедра"
    )

    disciplines = models.ManyToManyField(
        Discipline,
        related_name='specialties',
        verbose_name="Список дисциплін"
    )

    def __str__(self):
        return f"{self.code} - {self.name}"


class Teacher(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=120, verbose_name="Імʼя")
    position = models.CharField(max_length=100, verbose_name="Посада")
    degree = models.CharField(max_length=100, verbose_name="Ступінь")

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='teachers',
        verbose_name="Кафедра"
    )

    def __str__(self):
        return f"{self.position} {self.name}"
