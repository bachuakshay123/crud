from django.shortcuts import render,redirect
from crud_app.models import student
from crud_app.forms import studentForms
from django.core.paginator import Paginator
from django.db.models import Q


def home(request):
    form=studentForms()
    if request.method=="POST":
        form=studentForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form=studentForms()
    return render(request, "Enter_details.html",{'form':form})

def view_data(request):
    search = request.GET.get('search', '')
    data = student.objects.all()
    if search:
        data = data.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(email__icontains=search)
        )
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'view.html', {
        'page_obj': page_obj,
        'search': search
    })

def edit_data(request, id):
    data = student.objects.get(id=id)
    if request.method == 'POST':
        form = studentForms(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form = studentForms(instance=data)
    return render(request, 'Enter_details.html', {'form': form})

def delete_data(request, id):
    data = student.objects.get(id=id)
    data.delete()
    return redirect('view')