from django.shortcuts import render
from c_app.forms import NewUserForm

# Create your views here.
def front_page(request):
    return render(request, 'c_app/front_page.html')

def about_page(request):
    return render(request, 'c_app/about_page.html')

def join_page(request):
    form = NewUserForm()
    if request.method=='POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return login_succ(request)
        else:
            print("ERROR! Please recheck your details.")

    return render(request, 'c_app/join_page.html',{'form':form})

def login_succ(request):
    return render(request, 'c_app/login_succ.html')

def event_page(request):
    return render(request, 'c_app/event_page.html')
