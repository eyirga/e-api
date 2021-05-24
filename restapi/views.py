from django.shortcuts import render, redirect
from .models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *

# ==================================== PRODUCT ================================== #

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductListViewSet(viewsets.ModelViewSet):
    queryset = ProductList.objects.all()
    serializer_class = ProductListSerializer

class OrderCatgoryViewSet(viewsets.ModelViewSet):
    queryset = OrderCatgory.objects.all()
    serializer_class = OrderCatgorySerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer            

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer            

# ==================================== CUSTOMER ================================== #
class CustomerCategoryViewSet(viewsets.ModelViewSet):
    queryset = CustomerCategory.objects.all()
    serializer_class = CustomerCategorySerializer    

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer    

# ==================================== EMPLOYEE ================================== #
class EmployeeCategoryViewSet(viewsets.ModelViewSet):
    queryset = EmployeeCategory.objects.all()
    serializer_class = EmployeeCategorySerializer      

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer      

# ==================================== TUTORIAL ================================== #
class TutorialViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

class TutorialCategoryViewSet(viewsets.ModelViewSet):
    queryset = TutorialCategory.objects.all()
    serializer_class = TutorialCategorySerializer

# ==================================== BOOK ================================== #
class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ==================================== RESTAURANT ================================== #
class RestaurantCategoryViewSet(viewsets.ModelViewSet):
    queryset = RestaurantCategory.objects.all()
    serializer_class = RestaurantCategorySerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantReviewViewSet(viewsets.ModelViewSet):
    queryset = RestaurantReview.objects.all()
    serializer_class = RestaurantReviewSerializer

class ServiceTimeViewSet(viewsets.ModelViewSet):
    queryset = ServiceTime.objects.all()
    serializer_class = ServiceTimeSerializer

class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer    

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer    

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderRestViewSet(viewsets.ModelViewSet):
    queryset = OrderRest.objects.all()
    serializer_class = OrderRestSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = DiscountSerializer

class PartnerRestaurantViewSet(viewsets.ModelViewSet):
    queryset = PartnerRestaurant.objects.all()
    serializer_class = PartnerRestaurantSerializer

class SellViewSet(viewsets.ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
# ===================================== Contact ========================================= #
class ContactCategoryViewSet(viewsets.ModelViewSet):
    queryset = ContactCategory.objects.all()
    serializer_class = ContactCategorySerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# ==================================== TASK AND TASK CATEGORIES ===========================#
class TaskCategoryViewSet(viewsets.ModelViewSet):
    queryset = TaskCategory.objects.all()
    serializer_class = TaskCategorySerializers

class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializers

# ==================================== CLIENT ===========================#
class ClientCategoryViewSet(viewsets.ModelViewSet):
    queryset = ClientCategory.objects.all()
    serializer_class = ClientCategorySerializers

class ClientListViewSet(viewsets.ModelViewSet):
    queryset = ClientList.objects.all()
    serializer_class = ClientListSerializers
    
# ==================================== ALBUM ===========================#
class AlbumCategoryViewSet(viewsets.ModelViewSet):
    queryset = AlbumCategory.objects.all()
    serializer_class = AlbumCategorySerializers

class AlbumListViewSet(viewsets.ModelViewSet):
    queryset = AlbumList.objects.all()
    serializer_class = AlbumListSerializers
        