from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views.generic import TemplateView
import json

from . models import Character, Tierlist
from . forms import TierForm

class IndexView(TemplateView):
    template_name = 'tekkentiers/index.html'

    def get(self, request):
        form = TierForm()
        character_list = Character.objects.order_by('character_name')
        content = {'character_list': character_list, 'form': form}
        return render(request, self.template_name, content)
        
    def post(self, request):
        form = TierForm(request.POST)
        if form.is_valid():
            tierData = form.cleaned_data['post']
            form = TierForm()

            """ Make a Tierlist model """
            newTierlist = Tierlist()
            newTierlist.tierlist = tierData
            newTierlist.save()

            tierData = json.loads(tierData)

            tiers = tierData['tier']
            rows = []
            
            del tierData['tier']

            for value in tierData.values():
                rows.append(value)

        character_list = Character.objects.order_by('character_name')
        content = {'character_list': character_list, 'tiers': zip(tiers, rows), 'rows': rows}
        return render(request, 'tekkentiers/sharelist.html', content)

def shareList(request, list_id):
    character_list = Character.objects.order_by('character_name')
    try:
        tierData = Tierlist.objects.get(pk=list_id)
        tierData = json.loads(tierData.tierlist)

        tiers = tierData['tier']
        rows = []
    
        
        del tierData['tier']

        for value in tierData.values():
            rows.append(value)
        

    except Tierlist.DoesNotExist:
        raise Http404("The Tierlist does not exist!")

    content = {'character_list': character_list, 'tiers': zip(tiers, rows), 'rows': rows}
    return render(request, 'tekkentiers/sharelist.html', content)

