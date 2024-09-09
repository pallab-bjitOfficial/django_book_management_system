from django.db.models import Q


def generate_filter(request):
    author_name = request.query_params.get('author')
    book_name = request.query_params.get('title')
    price = request.query_params.get('price')
    filters = Q()
    if author_name:
        filters &= Q(author__name=author_name)
    if book_name:
        filters &= Q(title__icontains=book_name)
    if price:
        filters &= Q(price__gte=price)
    return filters
