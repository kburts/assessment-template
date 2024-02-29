from rest_framework import serializers

from .models import Order

from rest_framework import viewsets
from rest_framework.response import Response

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product', 'customer', 'quantity']

  # POST /orders {"product": 5, "customer": 17, "quantity" 30}


class OrderViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        order = serializer.savre()
        return Response()
      
    def update(self, request, pk=None):
        order = self.get_object()
        order.update(serializer.validated_data)
        order.save()

        return Response()
