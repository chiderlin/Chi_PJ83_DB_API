from django.db import models

# Create your models here.
class DomainListAll(models.Model):
    """
    a migrate --fake table.
    """
    id = models.AutoField(primary_key=True)
    AgentID = models.CharField(max_length=30, unique=True)
    CodeToMatch = models.CharField(max_length=50, unique=True)
    DomainListAPP = models.CharField(max_length=300)
    DomainListInner = models.CharField(max_length=300)
    DomainListOuter = models.CharField(max_length=300)
    CreatedTime = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = "DomainListAll"


class DomainTestLog(models.Model):
    """
    a migrate --fake table.
    """
    TestTime = models.DateTimeField(blank=True, null=True)
    UrlIn = models.CharField(max_length=200)
    UrlOut = models.CharField(max_length=200)
    MyIP = models.CharField(max_length=200)
    MyZone = models.CharField(max_length=200)
    CDN = models.CharField(max_length=200)
    CDNIP = models.CharField(max_length=200)
    PageLoadTime = models.FloatField()
    Status = models.CharField(max_length=50)
    IPScreenshot = models.CharField(max_length=300)
    ProductScreenshot1 = models.CharField(max_length=300)
    ProductScreenshot2 = models.CharField(max_length=300)
    ProductScreenshot3 = models.CharField(max_length=300)
    ProductScreenshot4 = models.CharField(max_length=300)
    CreatedTime = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = "DomainTestLog"
