from django.shortcuts import render
from django.views import View
import platform
# Create your views here.

class HomeView(View):

    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {
            'greeting' : "Hello",
            'computername': platform.node(),
        }
        
        return render(request, self.template_name, context)

