from rest_framework import serializers
from django.db import transaction
from .models import Order, OrderItem
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ['product', 'product_name', 'quantity', 'price']
        read_only_fields = ['price'] 

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'status', 'total_price', 'created_at']
        read_only_fields = ['total_price', 'status']

    def validate(self, data):
        """
        Check if there is enough stock for all items.
        """
        items_data = data.get('items')
        if not items_data:
            raise serializers.ValidationError("No items in order.")

        for item in items_data:
            product = item['product']
            quantity = item['quantity']
            if product.stock_quantity < quantity:
                raise serializers.ValidationError(
                    f"Not enough stock for {product.name}. Available: {product.stock_quantity}, Requested: {quantity}"
                )
        return data

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user
        
        with transaction.atomic():
            order = Order.objects.create(user=user, **validated_data)
            total_price = 0

            for item_data in items_data:
                product = item_data['product']
                quantity = item_data['quantity']
                
                # Deduct stock
                product.stock_quantity -= quantity
                product.save()

                # Lock price at purchase time
                price = product.price
                OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
                total_price += price * quantity
            
            order.total_price = total_price
            order.save()
        
        return order
