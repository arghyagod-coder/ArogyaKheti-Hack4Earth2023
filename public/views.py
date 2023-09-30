from django.shortcuts import render
from dashboard.models import Produce

# Create your views here.
def view_listings_page(request):
    products = Produce.objects.all()
    context = {
        'products': products,
    }
    return render(request, "dash/market/market_produce.html", context)