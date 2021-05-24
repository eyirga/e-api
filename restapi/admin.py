from django.contrib.auth.admin import UserAdmin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# =========================== USER ================================= #
admin.site.register(User, UserAdmin)

# =========================== PRODUCT SECTION ================================= #
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name")

class ProductListAdmin(admin.ModelAdmin):
    list_display = ("list")

class OrderCatgoryAdmin(admin.ModelAdmin):
    list_display = '__all__'    

class OrderAdmin(admin.ModelAdmin):
    list_display = '__all__'    

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = '__all__'    

@admin.register(ProductCategory)
class CategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(ProductList)
class ListingAdmin(ImportExportModelAdmin):
    pass

@admin.register(OrderCatgory)
class OrderCatgoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    pass

@admin.register(OrderDetail)
class OrderDetailAdmin(ImportExportModelAdmin):
    pass

# ============================= RESTAURANT SECTION ================================ #

@admin.register(RestaurantCategory)
class RestaurantCategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(Restaurant)
class RestaurantAdmin(ImportExportModelAdmin):
	pass

@admin.register(ServiceTime)
class ServiceTimeAdmin(ImportExportModelAdmin):
	pass

@admin.register(RestaurantReview)
class RestaurantReviewAdmin(ImportExportModelAdmin):
	pass

@admin.register(FoodCategory)
class FoodCategoryAdmin(ImportExportModelAdmin):
	pass

@admin.register(Food)
class FoodAdmin(ImportExportModelAdmin):
	pass

@admin.register(Division)
class DivisionAdmin(ImportExportModelAdmin):
	pass

@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
	pass

@admin.register(Notification)
class NotificationAdmin(ImportExportModelAdmin):
	pass
@admin.register(Cart)
class CartAdmin(ImportExportModelAdmin):
	pass
@admin.register(OrderRest)
class OrderRestAdmin(ImportExportModelAdmin):
	pass
@admin.register(Discount)
class DiscountAdmin(ImportExportModelAdmin):
	pass
@admin.register(PartnerRestaurant)
class PartnerRestaurantAdmin(ImportExportModelAdmin):
	pass
@admin.register(Sell)
class SellAdmin(ImportExportModelAdmin):
	pass
@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
	pass

# =============== CUSTOMER ======================== #
class CustomerCategoryAdmin(admin.ModelAdmin):
    list_display = '__all__'    

class CustomerAdmin(admin.ModelAdmin):
    list_display = '__all__'    

@admin.register(CustomerCategory)
class CustomerCategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    pass

# =============== EMPLOYEE ======================== #
class EmployeeCategoryAdmin(admin.ModelAdmin):
    list_display = '__all__'    

class EmployeeAdmin(admin.ModelAdmin):
    list_display = '__all__'    

@admin.register(EmployeeCategory)
class EmployeeCategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    pass

# =============== CONTACT ======================== #
@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
	pass

@admin.register(ContactCategory)
class ContactCategoryAdmin(ImportExportModelAdmin):
	pass

# =============== TUTORIAL ======================== #
class TutorialCategoryAdmin(admin.ModelAdmin):
    list_display = ("name")

class TutorialAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "published")

@admin.register(TutorialCategory)
class TutorialCategoryAdmin(ImportExportModelAdmin):
	pass

@admin.register(Tutorial)
class TutorialAdmin(ImportExportModelAdmin):
	pass

# =============== BOOK ======================== #
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ("name")

class BookAdmin(admin.ModelAdmin):
    list_display = ("title")

@admin.register(BookCategory)
class BookCategoryAdmin(ImportExportModelAdmin):
	pass

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
	pass

# =============== BLOG ======================== #
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name")

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title")

@admin.register(BlogCategory)
class BlogCategoryAdmin(ImportExportModelAdmin):
	pass

@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin):
	pass

# ================ TASK and TASK CATEGORIES ======================= #
class TaskListAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "due_date")

class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ("name")


@admin.register(TaskList)
class TaskListAdmin(ImportExportModelAdmin):
    pass

@admin.register(TaskCategory)
class TaskCategoryAdmin(ImportExportModelAdmin):
    pass

# ================ CLIENT ======================= #
class ClientCategoryAdmin(admin.ModelAdmin):
    list_display = ("name")

class ClientListAdmin(admin.ModelAdmin):
    list_display = ("first_name")

@admin.register(ClientCategory)
class ClientCategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(ClientList)
class TaskListAdmin(ImportExportModelAdmin):
    pass

# ================ ALBUM ======================= #
class AlbumCategoryAdmin(admin.ModelAdmin):
    list_display = ("name")

class AlbumListAdmin(admin.ModelAdmin):
    list_display = ("title")

@admin.register(AlbumCategory)
class AlbumCategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(AlbumList)
class AlbumListAdmin(ImportExportModelAdmin):
    pass

