from rest_framework import serializers
from .models import Admin, Vendor, Customer
from django.core import validators


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        exclude = ["is_vendor"]

    def create(self, validated_data, **kwargs):
        vendor = super().create(dict(is_vendor=True, **validated_data))
        return vendor


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        exclude = ["is_admin"]

    def create(self, validated_data, **kwargs):
        admin = super().create(dict(is_admin=True, **validated_data))
        return admin
