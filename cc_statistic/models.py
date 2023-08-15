import datetime

from django.utils import timezone
from django.db import models

# Create your models here.
# 'migrate' creates db, 'makemigrations' update db
# Import model: in Terminal, 'python manage.py inspectdb'


class ItSecChina(models.Model):
    company = models.CharField(db_column='company', max_length=45, blank=True, null=True)
    product = models.CharField(db_column='product', max_length=45, blank=True, null=True)
    certification = models.CharField(db_column='certification', max_length=45, blank=True, null=True)
    level = models.CharField(db_column='level', max_length=45, blank=True, null=True)
    issue_date = models.CharField(db_column='issue_date', max_length=45, blank=True, null=True)
    validation = models.CharField(db_column='validation', max_length=45, blank=True, null=True)
    remark = models.CharField(db_column='remark', max_length=45, blank=True, null=True)


class CommonCriteria(models.Model):
    category = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    manufacturer = models.TextField(blank=True, null=True)
    scheme = models.TextField(blank=True, null=True)
    assurance_level = models.TextField(blank=True, null=True)
    protection_profile = models.TextField(blank=True, null=True)
    certification_date = models.TextField(blank=True, null=True)
    archived_date = models.TextField(blank=True, null=True)
    certification_report_url = models.TextField(blank=True, null=True)
    security_target_url = models.TextField(blank=True, null=True)
    maintenance_date = models.TextField(blank=True, null=True)
    maintenance_title = models.TextField(blank=True, null=True)
    maintenance_report = models.TextField(blank=True, null=True)
    maintenance_st = models.TextField(blank=True, null=True)


class Niap(models.Model):
    product = models.TextField(blank=True, null=True)
    vid = models.CharField(max_length=45, blank=True, null=True)
    conformance_claim = models.CharField(max_length=200, blank=True, null=True)
    cctl = models.CharField(max_length=80, blank=True, null=True)
    certification_date = models.DateField(blank=True, null=True)
    assurance_maintenance_date = models.DateField(blank=True, null=True)
    scheme = models.CharField(max_length=45, blank=True, null=True)


class CcStatisticSpain(models.Model):
    name = models.CharField(unique=True, max_length=200, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    certification_date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_statistic_spain'


class CertifiedProducts(models.Model):
    category = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    manufacturer = models.TextField(blank=True, null=True)
    scheme = models.TextField(blank=True, null=True)
    assurance_level = models.TextField(blank=True, null=True)
    protection_profile = models.TextField(blank=True, null=True)
    certification_id = models.CharField(max_length=45, blank=True, null=True)
    certification_date = models.TextField(blank=True, null=True)
    archived_date = models.TextField(blank=True, null=True)
    certification_report_url = models.TextField(blank=True, null=True)
    security_target_url = models.TextField(blank=True, null=True)
    maintenance_date = models.TextField(blank=True, null=True)
    maintenance_title = models.TextField(blank=True, null=True)
    maintenance_report = models.TextField(blank=True, null=True)
    maintenance_st = models.TextField(blank=True, null=True)
    remark = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certified_products'