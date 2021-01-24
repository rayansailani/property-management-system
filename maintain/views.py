from django.shortcuts import render, redirect
from django.db import connection
from properties.models import PropertyForRent
# Create your views here.


def maintain_view(request, id):
    cursor = connection.cursor()
    property = PropertyForRent.objects.get(id=id)
    if request.POST:
        name = request.POST.get('name_id')
        ph_no = request.POST.get('ph_id')
        owner_id = request.user.id
        property_id = property.id
        cursor.execute("insert into maintainers_rent(name,ph_no,p_id,owner_id) values(%s,%s,%s,%s)", [
                       name, ph_no, property_id, owner_id])
        property.has_maintainer = True
        property.save()
        return redirect('dashboard')
    return render(request, 'maintain/maintain.html')
