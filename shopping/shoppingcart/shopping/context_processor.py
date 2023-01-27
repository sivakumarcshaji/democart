from . models import Category ,Product
def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)
def menu_links(request):
    links=Product.objects.all()
    return dict(links=links)