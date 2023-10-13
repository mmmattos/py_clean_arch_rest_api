from rest_framework import serializers
from theapp.domain.entities import User, Product, Order

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'email')

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'name', 'price')
	
class OrderSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	products = ProductSerializer(many=True)

class Meta:
	model = Order
	fields = ('id', 'user', 'products')
	
def create(self, validated_data):
	user_data = validated_data.pop('user')
	product_data = validated_data.pop('products')
	
	user = User.objects.get(id=user_data['id'])
	products = [Product.objects.get(id=product['id']) for product in product_data]

	order = Order.objects.create(user=user)
	order.products.set(products)

    return order 
