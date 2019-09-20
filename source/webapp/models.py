from django.db import models

STATUS_CHOICES = (
    ('new', 'новая'),
    ('in_progress', 'В процессе'),
    ('Finished', 'Завершена')
)


class Task(models.Model):
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='описание')
    status = models.CharField(max_length=40, null=False, blank=False, verbose_name="Статус",
                              default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
    date_perf = models.TextField(blank=True, default=" ", verbose_name='Время изменения',
                                 help_text="Use the following format: <em>YYYY-MM-DD</em>.")
    detail = models.TextField(max_length=350, blank=True, default=" ", verbose_name='Поробное описание')

    def __str__(self):
        return self.description
