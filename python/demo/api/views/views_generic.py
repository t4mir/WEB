# from rest_framework import mixins, views
# from rest_framework import generics
# from rest_framework.mixins import ListModelMixin
# from django.db.models.query import QuerySet
# from api.models import Category
# from api.serializers import CategorySerializer2
#
#
# class CategoryListAPIView(mixins.ListModelMixin,mixins.CreateModelMixin,
#                   GenericAPIView):
#
#
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer2
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return  self.create(request, *args, **kwargs)
#
#
# class CategoryDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                             mixins.DestroyModelMixin):
#     queryset = Category.object.all()
#     serializer_class = CategorySerializer2
#
#     #lookup_url_kwarg = 'category_id'
#
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)