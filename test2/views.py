from django.shortcuts import render
from .models import Blog
from .forms import SearchForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def home(request):
    form= SearchForm(request.POST or None)

    if form.is_valid():
        data= form.cleaned_data.get("search_field")
        
        blogs = Blog.objects.filter(title__contains=str(data))

        return render(request, "index_filter.html", context={'blogs':blogs})
        
    context={'form':form}

    return render(request, "index.html", context=context)

def blogs(request):
    blogs = Blog.objects.all()

    
    context={'blogs': blogs}

    return render(request, "blog.html", context=context)

def blog_content(request, pk):

    blog = get_object_or_404(Blog, pk=pk)
    context = {
        'blog':blog,
    }

    context={'blog': blog}
    return render(request, 'blog_content.html', context)