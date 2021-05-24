from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restapi import views

router = routers.DefaultRouter()
router.register('ProductCagtegory', views.ProductCategoryViewSet)
router.register('ProductList', views.ProductListViewSet)
router.register('OrderCatgory', views.OrderCatgoryViewSet)
router.register('Customer', views.CustomerViewSet)
router.register('CustomerCategory', views.CustomerCategoryViewSet)
router.register('Employee', views.EmployeeViewSet)
router.register('EmployeeCategory', views.EmployeeCategoryViewSet)
router.register('Order', views.OrderViewSet)
router.register('OrderDetail', views.OrderDetailViewSet)

router.register('TutorialCategory', views.TutorialCategoryViewSet)
router.register('Tutorial', views.TutorialViewSet)

router.register('BookCategory', views.BookCategoryViewSet)
router.register('Book', views.BookViewSet)

router.register('RestaurantCategory', views.RestaurantCategoryViewSet)
router.register('Restaurant', views.RestaurantViewSet)
router.register('RestaurantReview', views.RestaurantReviewViewSet)
router.register('ServiceTime', views.ServiceTimeViewSet)
router.register('FoodCategory', views.FoodCategoryViewSet)
router.register('Food', views.FoodViewSet)
router.register('Divistion', views.DivisionViewSet)
router.register('City', views.CityViewSet)
router.register('Notification', views.NotificationViewSet)
router.register('Cart', views.CartViewSet)
router.register('OrderRest', views.OrderViewSet)
router.register('Discount', views.DiscountViewSet)
router.register('PartnerRestaurant', views.PartnerRestaurantViewSet)
router.register('Sell', views.SellViewSet)
router.register('Review', views.ReviewViewSet)

router.register('ContactCategory', views.ContactCategoryViewSet)
router.register('Contact', views.ContactViewSet)

router.register('TaskCategory', views.TaskCategoryViewSet)
router.register('Tasklist', views.TaskListViewSet)

router.register('ClientCategory', views.ClientCategoryViewSet)
router.register('ClientList', views.ClientListViewSet)

router.register('AlbumCategory', views.AlbumCategoryViewSet)
router.register('AlbumList', views.AlbumListViewSet)

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
