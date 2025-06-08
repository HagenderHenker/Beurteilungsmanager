from django.shortcuts import render, HttpResponse
from beurteilung.forms import BeurteilungForm
from beurteilung.models import Beurteilungen,  Beurteilungstemplate, Beurteilungsgliederung, Beurteilungsauspraegungen
# Create your views here.

def index(request):

    """
    Index view for the application.
    """
    return render(request, 'index.html', {})

# Templates

def beurteilungstemplates_list(request):
    """
    View to list all Beurteilung templates.
    """
   
    beurteilungstemplates = Beurteilungstemplate.objects.all()
    print(beurteilungstemplates)
    
    for element in beurteilungstemplates:
        print(element)

    return render(request, 'beurteilungstemplate/beurteilungstemplates_list.html', {'beurteilungstemplates': beurteilungstemplates})

def beurteilungstemplates_detail(request, template_id):
    """
    View to display details of a specific Beurteilung template.
    """
    # This is a placeholder for the actual logic to retrieve a specific Beurteilung template by ID.
    return HttpResponse(f"Details of Beurteilung template with ID {template_id} will be displayed here.")

def beurteilungsgliederung_list(request):
    """
    View to list all Beurteilung gliederungen.
    """
    # This is a placeholder for the actual logic to retrieve Beurteilung gliederungen.
    return HttpResponse("List of Beurteilung gliederungen will be displayed here.")

def beurteilungsgliederung_detail(request, gliederung_id):
    """
    View to display details of a specific Beurteilung gliederung.
    """
    # This is a placeholder for the actual logic to retrieve a specific Beurteilung gliederung by ID.
    return HttpResponse(f"Details of Beurteilung gliederung with ID {gliederung_id} will be displayed here.")   

def beurteilungsauspraegungen_list(request):
    """
    View to list all Beurteilung auspraegungen.
    """
    # This is a placeholder for the actual logic to retrieve Beurteilung auspraegungen.
    return HttpResponse("List of Beurteilung auspraegungen will be displayed here.")       

def beurteilungen_list(request):
    """
    View to list all Beurteilungen.
    """


    beurteilungen = Beurteilungen.objects.all()
    print(beurteilungen)


    return render(request, 'beurteilung/beurteilungen_list.html', {'beurteilungen': beurteilungen})

0

def beurteilung_new(request):
    """
    View to handle Beurteilung form submission.
    """
    if request.method == 'POST':
        form = BeurteilungForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
            return HttpResponse("Beurteilung submitted successfully.")
    else:
        form = BeurteilungForm()

    return render(request, 'beurteilung_form.html', {'form': form})