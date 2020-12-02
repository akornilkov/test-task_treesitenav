from django.http import JsonResponse
from .controllers import get_all_navigation_items, get_all_domains
from .serializers import NavigationItemSerializer, DomainModelSerializer


def navigation_item_view(request):
    return JsonResponse(NavigationItemSerializer(get_all_navigation_items('home')).data)


def domain_model_view(request):
    return JsonResponse(DomainModelSerializer(get_all_domains('ru')).data)
