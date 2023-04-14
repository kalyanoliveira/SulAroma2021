from django.shortcuts import render
# Import app-level models.py classes to interact with database
from schedule.models import event

# Create your views here.

# Index function that is called by app-level urls.py
def index(request):
    if event.objects.exists():

        events = event.objects.all() # Fetch all current events from database
        templateArray = []
        
        for i in events:

            # Convert one event's data into strings, these which are saved in individual variables
            tempWhenStart = i.whenStart.strftime("%d %b, %H:%M")
            tempWhenEnd = i.whenEnd.strftime("%H:%M")
            tempWhen = f"{tempWhenStart} - {tempWhenEnd}"
            tempName = i.name
            tempDescription = i.description

            # Create new array of formatted strings relating to event's information, using the definitions above
            tempArray = [tempWhen, tempName, tempDescription]
            
            # Append created array to main events array (which is 2D)
            templateArray.append(tempArray)

        # HttpResponse of schedule/index.html
        return render(request, "schedule/index.html", {
            'pageName':'Schedules',
            'events':templateArray # Formatted string array, with data for events' information
        })
    
    else: # No events exist

        # HttpResponse of schedule/index.html
        return render(request, "schedule/index.html", {
            'pageName':'Schedules',
            'events':[] # Empty events data array
        })