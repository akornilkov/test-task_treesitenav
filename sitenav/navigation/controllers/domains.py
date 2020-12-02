from ..models import DomainModel


def get_all_domains(name='ru'):
    """Получение всего дерева доменов"""
    return DomainModel.objects.get(name=name)
