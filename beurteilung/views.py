from django.shortcuts import render, HttpResponse, get_object_or_404
from beurteilung.forms import BeurteilungForm, BeurteilungstemplateForm
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
    template = get_object_or_404(Beurteilungstemplate, id=template_id)
    form = BeurteilungstemplateForm(instance=template)
    

    if request.method == 'POST':
        form = BeurteilungstemplateForm(request.POST or None, instance=template)
        if form.is_valid():
            form.save()
            return HttpResponse("Beurteilung template updated successfully.")
        
    return render(request, 'beurteilungstemplate/beurteilungstemplates_detail.html', {'form': form})


    

    
    return render(request, 'beurteilungstemplate/beurteilungstemplates_update.html', {} )

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