from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.

def index(request):
    Cycle = Item.objects.filter().all()
    buyers = Buyer.objects.filter().all()
    sellers = Seller.objects.filter().all()
    context = {"CYCLE": Cycle, "buyers": buyers, "sellers": sellers}
    return render(request, "index.html", context=context)


def cycle(request, form_data=None):
    if request.method == "POST":
        form_data - ItemForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            item = form_data.save(commit=False)
            item = request.user
            item.save("cycle")
    queryset = Item.objects.filter()
    context = {"bikes": queryset, "form": ItemForm}
    return render(request, "CYCLE.html", context=context)

def bikes(request, form_data=None):
    if request.method == "POST":
        form_data - ItemForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            item = form_data.save(commit=False)
            item = request.user
            item.save("cycle")
    queryset = Item.objects.filter()
    context = {"bikes": queryset, "form": ItemForm}
    return render(request, "bikes.html", context=context)

def bike(request, form_data=None):
    if request.method == "POST":
        form_data - ItemForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            item = form_data.save(commit=False)
            item = request.user
            item.save("cycle")
    queryset = Item.objects.filter()
    context = {"bike": queryset, "form": ItemForm}
    return render(request, "bike.html", context=context)


def buy(request, form_data=None):
    if request.method == "POST":
        form_data - ItemForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            item = form_data.save(commit=False)
            item = request.user
            item.save("cycle")
    queryset = Item.objects.filter()
    context = {"buy": queryset, "form": ItemForm}
    return render(request, "buy.html", context=context)

def buy2(request, form_data=None):
    if request.method == "POST":
        form_data - ItemForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            item = form_data.save(commit=False)
            item = request.user
            item.save("cycle")
    queryset = Item.objects.filter()
    context = {"buy2": queryset, "form": ItemForm}
    return render(request, "buy2.html", context=context)

def login(request, form_data=None):
    if request.method == "POST":
        form_data - ItemForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            item = form_data.save(commit=False)
            item = request.user
            item.save("cycle")
    queryset = Item.objects.filter()
    context = {"login": queryset, "form": ItemForm}
    return render(request, "login.html", context=context)

def signup(request, form_data=None):
    if request.method == "POST":
        form_data - ItemForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            item = form_data.save(commit=False)
            item = request.user
            item.save("cycle")
    queryset = Item.objects.filter()
    context = {"signup": queryset, "form": ItemForm}
    return render(request, "signup.html", context=context)