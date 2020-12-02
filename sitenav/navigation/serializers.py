from rest_framework import serializers
from unicef_restlib.fields import WriteListSerializeFriendlyRecursiveField
from unicef_restlib.serializers import WritableNestedSerializerMixin, RecursiveListSerializer

from .models import NavigationItem, DomainModel


class NavigationItemSerializer(WritableNestedSerializerMixin, serializers.ModelSerializer):
    children = RecursiveListSerializer(
        child=WriteListSerializeFriendlyRecursiveField(required=False),
        required=False
    )

    class Meta(WritableNestedSerializerMixin.Meta):
        model = NavigationItem
        fields = ("id", "name", "children", "f_path")


class DomainModelSerializer(WritableNestedSerializerMixin, serializers.ModelSerializer):
    subdomains = RecursiveListSerializer(
        child=WriteListSerializeFriendlyRecursiveField(required=False),
        required=False
    )

    class Meta(WritableNestedSerializerMixin.Meta):
        model = DomainModel
        fields = ("id", "name", "subdomains", "full_name", "level")
