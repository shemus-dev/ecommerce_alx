from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'head'] # Restrict updates/deletes if you want orders to be immutable, but CRUD implies all. 
    # Let's allow all for now, but usually orders shouldn't be deleted so easily. 
    # Requirement: "Users Management (CRUD)"... wait, "Product Management (CRUD)". 
    # For orders, usually just Place and List. I'll stick to full CRUD but user can only see their own.

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')
    
    def perform_create(self, serializer):
        # We handled user assignment in serializer.create, but standard is here.
        # However, our serializer logic needs 'user' inside create() for the transaction.
        # So we don't need to do anything special here as long as serializer has context['request'].
        serializer.save()
