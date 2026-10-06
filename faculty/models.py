from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    head_of_department = models.CharField(max_length=255, verbose_name="Завідувач кафедри")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедри"


class Specialty(models.Model):
    DEGREE_CHOICES = [
        ('bachelor', 'Бакалаврат'),
        ('master', 'Магістратура'),
        ('phd', 'Аспірантура'),
    ]

    name = models.CharField(max_length=255, verbose_name="Назва (Освітня програма)")
    code = models.CharField(max_length=50, verbose_name="Код спеціальності")
    educ_program = models.CharField(max_length=50, verbose_name="Освітня програма")
    degree = models.CharField(max_length=20, choices=DEGREE_CHOICES, default='bachelor',
                              verbose_name="Рівень вищої освіти")

    description = models.TextField(verbose_name="Опис")
    coordinator_name = models.CharField(max_length=255, verbose_name="Імʼя координатора набору")
    coordinator_contact = models.CharField(max_length=255, verbose_name="Контакт координатора набору")

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='specialties',
        verbose_name="Випускова кафедра"
    )
    disciplines = models.TextField(
        verbose_name="Що вивчається / Чого навчишся",
        default='', blank=True
    )

    def __str__(self):
        return f"{self.get_degree_display()} | {self.code} - {self.name}"

    class Meta:
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"


class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name="Імʼя")
    position = models.CharField(max_length=255, verbose_name="Посада")
    degree = models.CharField(max_length=255, verbose_name="Ступінь")
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='teachers',
        verbose_name="Кафедра"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"


class HomePageContent(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок", default="Головна сторінка")
    text = models.TextField(verbose_name="Текст головної сторінки")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Текст головної сторінки"
        verbose_name_plural = "Налаштування головної сторінки"

from datetime import date

class ExchangeProgram(models.Model):
    university = models.CharField(max_length=255, verbose_name="Університет")
    languages = models.CharField(max_length=255, verbose_name="Мови навчання")
    places = models.IntegerField(verbose_name="Кількість місць")
    deadline = models.DateField(verbose_name="Дедлайн подачі")
    description = models.TextField(verbose_name="Опис")
    country = models.CharField(max_length=100, verbose_name="Країна", default="")


    @property
    def is_active(self):
        return self.deadline >= date.today()

    def __str__(self):
        return self.university

    class Meta:
        verbose_name = "Програма обміну"
        verbose_name_plural = "Програми обміну"
