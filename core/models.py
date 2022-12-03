from django.db import models

OPTIONS = (
    ('telco', 'Telecommunication'),
    ('log', 'Logistics'),
    ('agr', 'Agriculture'),
    ('aero', 'Aerospace'),
    ('pharm', 'Pharmaceutical'),
)


class Company(models.Model):
    name = models.CharField(max_length=255)
    company_type = models.CharField(max_length=15, choices=OPTIONS)
    founded = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
