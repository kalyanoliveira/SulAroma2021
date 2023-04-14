from django.shortcuts import render
# Import app-level models.py classes to interact with database
from .models import speaker

# Create your views here.

# Index function that is called by app-level urls.py
def index(request):
    # HttpResponse of contact/index.html
    return render(request, "contact/index.html", {
        'pageName':'Contact',
        'speakers': speaker.objects.all() # Array of speaker's data
    })