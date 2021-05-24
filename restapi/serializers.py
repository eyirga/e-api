from rest_framework import serializers
from .models import *

# ===================== PRODUCT ======================= #
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductList
        fields = '__all__'

class OrderCatgorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCatgory
        fields = '__all__'        

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'   

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'   

# ===================================== RESTAURANT ========================================= #
class RestaurantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantCategory
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class RestaurantReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantReview
        fields = '__all__'

class ServiceTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTime
        fields = '__all__'

class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrderRestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderRest
        fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class PartnerRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerRestaurant
        fields = '__all__'

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = '__all__'                 

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'                           

# ===================================== CONTACT ========================================= #
class ContactCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactCategory
        fields = '__all__'        

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'        

# ===================================== TUTORIAL ========================================= #
class TutorialCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorialCategory
        fields = '__all__'

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = '__all__'

# ===================================== BOOK ========================================= #
class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = '__all__'                  

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'                  

# =============================== TASK AND TASK CATEGORIES ============================== #
class TaskCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
        fields = '__all__'


class TaskListSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskList  
        fields = '__all__'      

# =============================== CLIENT ============================== #
class ClientCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = ClientCategory
        fields = '__all__'


class ClientListSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClientList  
        fields = '__all__'              

# =============================== PICTURE ============================== #
class AlbumCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = AlbumCategory
        fields = '__all__'


class AlbumListSerializers(serializers.ModelSerializer):
    class Meta:
        model = AlbumList  
        fields = '__all__'           

# =============================== Customer ============================== #
class CustomerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCategory
        fields = '__all__'  

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'  

# =============================== Employee ============================== #
class EmployeeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCategory
        fields = '__all__'  

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'  
