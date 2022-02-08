from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy

from .forms import PetForm, OwnersForm
from .models import Pets, Owners

from django.contrib.auth import get_user_model
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()


@login_required(login_url="/login/")
def SearchView(request):
    if request.method == 'POST':
        searched = request.POST['searched']

        pets = Pets.objects.filter(name__contains=searched)
        owners = Owners.objects.filter(name__contains=searched)

        return render(request, 'search.html', {'pets': pets,
                                               'owners': owners,
                                               'searched': searched
                                               })

    else:
        return render(request, 'search.html', {})


@login_required(login_url="/login/")
def HomeView(request):
    labels = []
    data = []

    pets = Pets.objects.all()
    owners = Owners.objects.all()

    for owner in owners:
        labels.append(owner.name)
        data.append(owner.pet.count())
    return render(request, 'index.html', {'data': data, 'labels': labels

    })


@login_required(login_url="/login/")
def PetView(request):
    pets = Pets.objects.all()

    return render(request, 'pets_index.html', {
        'pets': pets

    })


@login_required(login_url="/login/")
def PetAddView(request):
    msg_success = None
    msg_fail = None
    success = False
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            msg_success = 'Added'

            return redirect("pets")

        else:
            msg_fail = 'Invalid form'
    else:
        form = PetForm()
    return render(request, 'pet_add.html',
                  {"form": form, "msg_success": msg_success, "msg_fail": msg_fail, "success": success})


@login_required(login_url="/login/")
def PetDetailView(request, pk):
    pet = Pets.objects.get(id=pk)
    return render(request, 'pets_detail.html', {'pet': pet})


@login_required(login_url="/login/")
def PetUpdateView(request, pk):
    instance = get_object_or_404(Pets, id=pk)
    form = PetForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('pets')

    return render(request, 'pet_update.html', {'form': form})


@permission_required('main.delete_pets')
def PetDeleteView(request, pk):
    # fetch the object related to passed id
    object = get_object_or_404(Pets, id=pk)

    if request.method == "POST":
        # delete object
        object.delete()
        # after deleting redirect to
        return redirect("pets")

    return render(request, "pet_delete.html", {'object': object})


@login_required(login_url="/login/")
def OwnerView(request):
    owners = Owners.objects.all()

    return render(request, 'owners_index.html', {'owners': owners

                                                 })


@login_required(login_url="/login/")
def OwnerAddView(request):
    msg_success = None
    msg_fail = None
    success = False
    if request.method == "POST":
        form = OwnersForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            msg_success = 'Added'

            return redirect("owners")

        else:
            msg_fail = 'Invalid form'
    else:
        form = OwnersForm()
    return render(request, 'owner_add.html',
                  {"form": form, "msg_success": msg_success, "msg_fail": msg_fail, "success": success})


@login_required(login_url="/login/")
def OwnerDetailView(request, pk):
    owner = Owners.objects.get(id=pk)
    return render(request, 'owner_detail.html', {'owner': owner})


@login_required(login_url="/login/")
def OwnerUpdateView(request, pk):
    instance = get_object_or_404(Owners, id=pk)
    form = OwnersForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('owners')

    return render(request, 'owner_update.html', {'form': form})


@permission_required('main.delete_pets')
def OwnerDeleteView(request, pk):
    # fetch the object related to passed id
    object = get_object_or_404(Owners, id=pk)

    if request.method == "POST":
        # delete object
        object.delete()
        # after deleting redirect to
        return redirect("owners")

    return render(request, "owner_delete.html", {'object': object})
