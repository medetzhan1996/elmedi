from django.db import models
from directory.models import ICD, Hospital


# Базовый mixin
class BaseMixin(models.Model):
    title = models.CharField(max_length=180)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


# Пакеты
class HospitalPackage(BaseMixin):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='hospital_icd')


# Услуги пакета
class HospitalPackageICD(models.Model):
    hospital_package = models.ForeignKey(HospitalPackage, on_delete=models.CASCADE)
    icd = models.ForeignKey(ICD, on_delete=models.CASCADE)
    social_at_home_performed = models.BooleanField(default=False)
    social_primary_health_care_performed = models.BooleanField(default=False)
    social_clinical_diagnostic_performed = models.BooleanField(default=False)
    social_hospital_performed = models.BooleanField(default=False)
    vhi_at_home_performed = models.BooleanField(default=False)
    vhi_primary_health_care_performed = models.BooleanField(default=False)
    vhi_clinical_diagnostic_performed = models.BooleanField(default=False)
    vhi_hospital_performed = models.BooleanField(default=False)
    pay_at_home_performed = models.BooleanField(default=False)
    pay_primary_health_care_performed = models.BooleanField(default=False)
    pay_clinical_diagnostic_performed = models.BooleanField(default=False)
    pay_hospital_performed = models.BooleanField(default=False)
    is_perfomed = models.BooleanField(default=False)

    @staticmethod
    def check_availability(icd, field_name):
        hospital_package_icd = HospitalPackageICD.objects.filter(icd=icd).last()
        if hospital_package_icd and not getattr(hospital_package_icd, field_name):
            return False
        return True

