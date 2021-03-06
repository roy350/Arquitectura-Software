from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import TemplateView
from .models import Message
from datetime import datetime
from ipware import get_client_ip
import datetime





from polls.forms import Form

def index(request):
    ip, is_routable = get_client_ip(request)
    if request.method == "POST":
        #mutable = request.POST._mutable
        #request.POST._mutable = True
        #request.POST['pub_date'] = str(datetime.datetime.now())
        #request.POST._mutable = mutable
        #print("antes del cambio")
        #print(request.POST['pub_date'])
        #print(str(datetime.datetime.now()))
        #print("despues del cambio")
        form = Form(request.POST)
        if (request.POST['ip'] == ip):
            if form.is_valid():
                #print("antes de guardar")
                form.save()
                #print("despues de guardar")
                #return redirect('polls/index.html')

    latest_message_list = Message.objects.order_by('-pub_date')
    template = loader.get_template('polls/index.html')
    context = {
        'latest_message_list': latest_message_list,
        'ip' : ip,
    }
    return HttpResponse(template.render(context, request))









class Home(TemplateView):
    template_name = 'polls/index.html'

    def get(self,request):
        form = From()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            text = form.cleaned_data['post']
            form = Form()
            return redirect('polls:polls')

        args = {'form': form, 'text': text}
        return render(request, self.template_name,args)
