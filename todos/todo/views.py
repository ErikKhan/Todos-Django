from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import NewtodoForm

# Create your views here.
todos = []
def index(request):
    return render(request, "index.html", {
        "todos": todos
    })


def add(request):
    return render(request, "add.html", {
        "form": NewtodoForm()
    })

def add(request):

    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = NewtodoForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the todo from the 'cleaned' version of form data
            todo = form.cleaned_data["todo"]

            # Add the new todo to our list of todos
            todos.append(todo)

            # Redirect user to list of todos
            return HttpResponseRedirect(reverse("index"))

        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "add.html", {
                "form": form
            })

    return render(request, "add.html", {
        "form": NewtodoForm()
    })