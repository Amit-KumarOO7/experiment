from django.db import models
from experiment.models import Rootcaim
import OpenSSL.crypto as crypto

# Create your models here.

class Request(models.Model):
    common_name = models.CharField(max_length=264,blank=False, help_text='enter url')
    country_code = models.CharField(max_length=2, blank=True)
    state = models.CharField(max_length=64, blank=True)
    org_name = models.CharField(max_length=64, blank=True)
    org_unit = models.CharField(max_length=64, blank=True)
    email = models.EmailField()
    certificate = models.TextField(unique=True)
    
    def x509req(self):
        """
            return instance if x509certificate
        """
        if self.certificate:
            return crypto.load_certificate_request(crypto.FILETYPE_PEM,self.certificate)


class CSR(models.Model):
    csr_content = models.TextField()
    validity_time = models.IntegerField(help_text='Validity time in years')
    set_issuer = models.ForeignKey(Rootcaim,on_delete=models.CASCADE, to_field='certificate')
