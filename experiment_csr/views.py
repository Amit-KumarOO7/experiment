from urllib import response
from django.shortcuts import render

from experiment_csr.models import CSR
from experiment_csr.models import Rootcaim
from .forms import CSRForm, RequestForm
import OpenSSL.crypto as crypto

# Create your views here.

def RequestView(request):
    form = RequestForm()
    
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            print('Generating CSR')
            digest = 'sha256'
            req = crypto.X509Req()
            subj = req.get_subject()
            subj.CN = form.cleaned_data['common_name']
            subj.ST = form.cleaned_data['state']
            subj.C = form.cleaned_data['country_code']
            subj.O = form.cleaned_data['org_name']
            subj.OU = form.cleaned_data['org_unit']
            subj.emailAddress = form.cleaned_data['email']
            key = crypto.PKey()
            key.generate_key(crypto.TYPE_RSA,2048)
            req.set_pubkey(key)
            req.sign(key,digest)
            form.instance.certificate = crypto.dump_certificate_request(crypto.FILETYPE_TEXT,req)
            print(req)
            form.save()
    return render(request,'certreq_page.html',{'form':form})


def CSRView(request):
    form = CSRForm()

    if request.method == 'POST':
        form = CSRForm(request.POST)
        if form.is_valid():
            print("Creating certificate from csr")
            req = crypto.load_certificate_request(crypto.FILETYPE_PEM,form.cleaned_data['csr_content'])
            cert = crypto.X509()
            cert.gmtime_adj_notBefore(0)
            cert.gmtime_adj_notAfter(form.cleaned_data['validity_time']*365*86400)
            cert.set_subject(req.get_subject())
            # ca = Rootcaim.objects.filter(name=form.cleaned_data['set_issuer']).values()
            # print(ca)
            # cry = crypto.load_certificate(crypto.FILETYPE_PEM,ca[0]['certificate'])
            # print(cry)
            ca = Rootcaim.objects.get(name=form.cleaned_data['set_issuer'])
            cry = crypto.load_certificate(crypto.FILETYPE_PEM,ca.certificate)
            print(cry)
            cert.set_pubkey(req.get_pubkey())
            print("pass 5")
            print(form.cleaned_data['set_issuer'])    
            form.save()
    return render(request,'csr_page.html',{'form':form})

# def ContentView(request):



            


