from ..models import NavigationItem


def get_all_navigation_items(name='/'):
    """Получение всего дерева"""
    return NavigationItem.objects.get(name=name)
