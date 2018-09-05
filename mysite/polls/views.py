from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import TemplateView
from .models import Message
from datetime import datetime
from ipware import get_client_ip
import datetime
from django.utils.timezone import utc





from polls.forms import Form

def index(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():

            form.save()
            #return redirect('polls/index.html')

    latest_message_list = Message.objects.order_by('-pub_date')
    print(latest_message_list[0])
    print(latest_message_list[0].pub_date)
    now = datetime.datetime.utcnow().replace(tzinfo=awt)
    latest_message_list[0].pub_date = now
    print(now)
    print(latest_message_list[0].pub_date)
    template = loader.get_template('polls/index.html')
    ip, is_routable = get_client_ip(request)
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
