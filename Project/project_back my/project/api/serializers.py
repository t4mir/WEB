from rest_framework import serializers
from api.models import Category, Game, Company, User


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data.get('name'))
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        company = Company.objects.create(name=validated_data.get('name'))
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    salary = serializers.FloatField(default=0)

    def create(self, validated_data):
        game = Game.objects.create(name=validated_data.get('name'), description=validated_data.get('description'),
                                   salary=validated_data.get('salary'))
        return game

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.save()
        return instance


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GameModelSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    # company = CompanyModelSerializer(read_only=True)
    company_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Game
        fields = ('id', 'name', 'description', 'salary', 'image', 'category_id', 'company_id')


class CategoryModelSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class CategoryModelSerializer(serializers.ModelSerializer):
    games = GameModelSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'games')


class CompanyModelSerializer(serializers.ModelSerializer):
    games = GameModelSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'games')
