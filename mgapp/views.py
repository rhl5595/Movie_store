from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Movies
from .forms import MoviesForm
# Create your views here.
def index(request) :
    movie=Movies.objects.all()
    context={
        'movie_list':movie
    }
    return render ( request,'index.html',context )

def details(request,m_id):
    m=Movies.objects.get(id=m_id)
    return render(request,"det.html",{'m':m})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        dec = request.POST.get ( 'dec' )
        Year = request.POST.get ( 'Year' )
        Img = request.FILES['Img']
        movie=Movies(name=name,dec=dec,Year=Year,Img=Img)
        movie.save()

    return render(request,'add.html')
def update(request,id):
    movie=Movies.objects.get(id=id)
    form=MoviesForm(request.POST,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'del.html')