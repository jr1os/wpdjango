from django.shortcuts import render, HttpResponse
html_base = """
<h1>My Home Page</h1>
<ul>
    <li><a href="/">HOME</a></li>
    <li><a href="/about-me">ABOUT</a></li>
    <li><a href="/portfolio">PORTFOLIO</a></li>
    <li><a href="/contact">CONTACT</a></li>
</ul>
"""


def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about-me.html")

def contact(request):
    return render(request, "core/contact.html")