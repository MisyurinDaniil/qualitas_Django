from django.shortcuts import render

def blog_page(request):
    return render(request, './appBlog/blog.html')

def finalblogpage_page(request):
    return render(request, './appBlog/finalblogpage.html')