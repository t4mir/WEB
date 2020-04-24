from rest_framework import serializers

from api.models import Category, Product


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data.get('name'))
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance


class CategorySerializer2(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=200) если хотите повтавить ограничение
    class Meta:
        model = Category
        fields = ('id', 'name',)


class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer2(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'category_id')


class CategoryWithProductSerializer(serializers.ModelSerializer):
    # products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  по дефолту
    # products = serializers.StringRelatedField(many=True, read_only=True)
    #                             если использовать то надо прописать tostring в самом классе
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'products')
