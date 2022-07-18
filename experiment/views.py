from django.shortcuts import render
from django.views.generic import TemplateView
from matplotlib.style import context
from experiment.foms import RootcaimForm
from experiment.models import Rootcaim
import OpenSSL.crypto as crypto
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

def RootCAView(request):
    form = RootcaimForm()

    if request.method == 'POST':
        obj = Rootcaim()
        form = RootcaimForm(request.POST)
        if form.is_valid():
            print("Setting up ROOT CA and IMs")
        key = crypto.PKey()
        key.generate_key(crypto.TYPE_RSA,2048)
        cert = crypto.X509()
        cert.get_subject().CN = form.cleaned_data['common_name']
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(form.cleaned_data['validity_time']*365*86400)
        cert.get_subject().C = form.cleaned_data['country_code']
        cert.get_subject().ST = form.cleaned_data['state']
        cert.get_subject().O = form.cleaned_data['org_name']
        cert.get_subject().OU = form.cleaned_data['org_unit']
        cert.set_issuer(cert.get_subject())
        print(cert.get_subject())
        cert.set_pubkey(key)
        cert.sign(key,"sha256")    
        # form.save(commit=False)
        # form.cleaned_data['certificate'] = crypto.dump_certificate(crypto.FILETYPE_TEXT,cert) 
        # form.certificate =  crypto.dump_certificate(crypto.FILETYPE_TEXT,cert) 
        # form.save()
        obj.common_name = form.cleaned_data['common_name']
        obj.name = form.cleaned_data['name']
        obj.validity_time = form.cleaned_data['validity_time']
        obj.org_name = form.cleaned_data['org_name']
        obj.org_unit = form.cleaned_data['org_unit']
        obj.country_code = form.cleaned_data['country_code']
        obj.certificate = crypto.dump_certificate(crypto.FILETYPE_PEM,cert) 
        obj.save()
    return render(request,'rootca_page.html', {'form':form})    
