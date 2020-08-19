from django.shortcuts import render
from cowsayapp.models import CowInput
from .forms import CowsayForm
import subprocess


# Create your views here.
def index_view(request):
    if request.method == 'POST':
        form = CowsayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            history_cow = data.get("cowfield")
            CowInput.objects.create(
                cowfield=data.get("cowfield")
            )
            cow_process = subprocess.run(
                ['cowsay', history_cow], capture_output=True, text=True
            )
            print(cow_process.stdout)
            return render(request, "index.html", {"form": CowsayForm(), "cow_process": cow_process.stdout})

    form = CowsayForm()
    return render(request, 'index.html', {"form": form})


def history_view(request):
    cow_history = CowInput.objects.filter().order_by('-id')[:10]
    return render(request, 'history.html', {"cow_history": cow_history})
