from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render
from .forms import RstForm,ProductForm,CommentForm,PcommentForm
from .models import Test,Product,Post,Comment,Pcomment,Category
from django.core.paginator import Paginator

def index(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = RstForm(request.POST, request.FILES)
        if form.is_valid():
            test = Test(
                subject=form.cleaned_data["subject"],
                summary=form.cleaned_data["summary"],
                upload_date=form.cleaned_data["upload_date"],
                image=form.cleaned_data["image"],
                acount=form.cleaned_data["acount"],
            )
            test.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'testgallery.html', {'form': form, 'img_obj': img_obj})
    else:
        form = RstForm()
    return render(request, 'testgallery.html', {'form': form})

def cat(request):

    return render(request, 'act.html')

def showindex(request):
    tests = Test.objects.all().order_by('-upload_date')
    context = {
        "tests": tests,
    }
    return render(request, "showindex.html", context)

def showdetail(request,pk):
    tests = Test.objects.get(pk=pk)
    context={
        'tests':tests
    }
    return render(request, 'showdetail.html', context)

def structure(request):
    tests = Test.objects.all().order_by('-upload_date')
    context = {
        "tests": tests,
    }
    return render(request, "structure.html", context)


def product(request,pk):
    product = Product.objects.get(pk=pk)
    pcomments = Pcomment.objects.filter(product=product)

    if request.method == "POST":
        form = PcommentForm(request.POST)
        if form.is_valid():
            pcomment = Pcomment(
                name=form.cleaned_data["name"],
                content=form.cleaned_data["content"],
                product=product,
            )
            pcomment.save()

            context = {
               "product": product,
               "pcomments": pcomments,
               "form": form
                       }
            return render(request, "product.html", context)
    else:
        form=PcommentForm()
        context={
            "product":product,
            "form":form
        }
    return render(request, 'product.html',context)

def productshow(request):
    products=Product.objects.all().order_by('serial_number')
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "products": products,
        "page_obj": page_obj,
    }
    return render(request, "productshow.html", context)

def product_write(request):
    """Process images uploaded by users"""

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        new = form.save(commit=False)

        if form.is_valid():
            product = Product(
                serial_number=form.cleaned_data["serial_number"],
                name=form.cleaned_data["name"],
                image=form.cleaned_data["image"],
                content=form.cleaned_data["content"],
                price=form.cleaned_data["price"],
            )
            new.save()
            form.save_m2m()
            # Get the current instance object to display in the template
            img_obj = form.instance
            #return render(request, 'productshow.html', {'form': form, 'img_obj': img_obj, 'products':products})
            return redirect('productshow')  #새로고침 시 이전 값이 자동 저장되는 것을 막기 위해 redirect를 썼다
    else:
        form = ProductForm()
    return render(request, 'product_write.html', {'form': form})


@login_required
def gallery(request):
    tests = Test.objects.all().order_by('-upload_date')
    context = {
        "tests": tests,
    }
    return render(request, "showindex.html", context)

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    context = {"post": post,
               "comments": comments,
               "form": form}
    return render(request, "blog_detail.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

"""
def image_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'image_index.html', context)

def image_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project  # key:key value
    }
    return render(request, 'image_detail.html', context)



def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    context = {"post": post,
               "comments": comments,
               "form": form}
    return render(request, "blog_detail.html", context)

from .forms import NameForm

"""