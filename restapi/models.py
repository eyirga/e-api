from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.db.models.signals import pre_save, post_save
from general.functions import unique_order_id_generator, unique_slug_generator, unique_key_generator, getRandomCode

# ----------------------------- ACCOUNT -----------------------------------------------------------#
class User(AbstractUser):
    #name = models.CharField(max_length=100, default='')
	phone   = models.CharField(max_length=20, blank=True, null=True)
	city    = models.CharField(max_length=128, default='',blank=True)
	address	= models.CharField(max_length=256, default='', blank=True)
	
	pp = models.URLField('profile_photo', null=True, blank=True)
	
	width_field         = models.IntegerField(default=0)
	height_field        = models.IntegerField(default=0)
	notice_offer        = models.TextField(blank=True, default='')
	about_me            = models.TextField(blank=True, default=' ')
	activation_code     = models.CharField(max_length=32, blank=True, null=True)
	pass_change_code    = models.CharField(max_length=32, blank=True, null=True)


	def get_profile_url(self):
		return reverse('accounts:profile', kwargs={'pk': self.pk})

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = 'account'



def pre_save_receiver(sender, instance, *args, **kwargs):
	pass

pre_save.connect(pre_save_receiver, sender=User)

# ---------------------- SECTION ONE PRODUCTS ----------------------------------------------------------- #

class ProductCategory(models.Model):
    # Basic
    category_name               = models.CharField(max_length=50, blank=False, null=False, default="eService")
    image              = models.URLField(blank=True, null=True)
    phone	   		   = models.CharField(max_length=12, blank=True, null=True, default='')
    email      		   = models.CharField(max_length=50, blank=True, null=True, default='')

    # location/contact
    address			   = models.CharField(max_length=50, blank=True, null=True, default='')
    city               = models.CharField(max_length=15, blank=True, null=True, default='')
    state              = models.CharField(max_length=10, blank=True, null=True, default='')
    zipcode            = models.CharField(max_length=12, blank=True, null=True, default='')
    
    # Photos
    logo 	 		   = models.URLField(blank=True, null=True)
    profile 	 	   = models.URLField(blank=True, null=True)

    # Others
    is_active          = models.BooleanField(default=False)
    status             = models.BooleanField(default=False)
    created_at 		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)
    desc               = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category_name

class ProductList(models.Model):
    category_name       = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    list                = models.CharField(max_length=64)
    desc                = models.TextField()
    amt                 = models.DecimalField(max_digits=8, decimal_places=2)
    image               = models.URLField(blank=True, null=True)
    checked             = models.BooleanField(default=False)
    sold                = models.BooleanField(default=False)
    instock             = models.BooleanField(default=False)
    created_at 		    = models.DateTimeField(auto_now=True)
    updated_at		    = models.DateTimeField(auto_now=True)


# to view string representation of the data
    def __str__(self):
        return self.list

# ================================= CUSTOMER ================================= #
class CustomerCategory(models.Model):
    name            = models.CharField(max_length=100)
    image           = models.URLField(blank=True, null=True)
    desc            = models.TextField(blank=True)
    content         = models.TextField(blank=True)
    created_at 		= models.DateTimeField(auto_now=True)
    updated_at		= models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name

class Customer(models.Model):
    customer_category       = models.ForeignKey(CustomerCategory, on_delete=models.CASCADE)
    first_name              = models.CharField(max_length=100, blank=True, null=True)
    last_name               = models.CharField(max_length=100, blank=True, null=True)
    middle_name             = models.CharField(max_length=100, blank=True, null=True)
    contatct_id             = models.CharField(max_length=20, blank=True, null=True)
    gender                  = models.CharField(max_length=20, blank=True, null=True)
    age                     = models.IntegerField(default=0, blank=True, null=True)
    profile                 = models.URLField(blank=True, null=True)
    email                   = models.CharField(max_length=50, blank=True, null=True)
    phone_mobile            = models.CharField(max_length=20, blank=True, null=True)
    phone_home              = models.CharField(max_length=20, blank=True, null=True)
    phone_work              = models.CharField(max_length=20, blank=True, null=True)
    address	                = models.CharField(max_length=256, blank=True, null=True)
    city                    = models.CharField(max_length=50, blank=True, null=True)
    state	                = models.CharField(max_length=50, blank=True, null=True)
    zipcode                 = models.IntegerField(default=0, blank=True, null=True)
    status                  = models.BooleanField(default=False, blank=True, null=True)
    desc                    = models.TextField(blank=True, default=' ')
    addition_info_01        = models.CharField(max_length=50, blank=True, null=True)
    addition_info_02        = models.CharField(max_length=50, blank=True, null=True)
    addition_info_03        = models.CharField(max_length=50, blank=True, null=True)
    is_active               = models.BooleanField(default=True, blank=True, null=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

# ================================= EMPLOYEE ================================= #
class EmployeeCategory(models.Model):
    name        = models.CharField(max_length=100)
    image       = models.URLField(blank=True, null=True)
    desc        = models.TextField(blank=True)
    content     = models.TextField(blank=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Employee(models.Model):
    employee_category       = models.ForeignKey(EmployeeCategory, on_delete=models.CASCADE)
    first_name              = models.CharField(max_length=100, blank=True, null=True)
    last_name               = models.CharField(max_length=100, blank=True, null=True)
    middle_name             = models.CharField(max_length=100, blank=True, null=True)
    contatct_id             = models.CharField(max_length=20, blank=True, null=True)
    gender                  = models.CharField(max_length=20, blank=True, null=True)
    age                     = models.IntegerField(default=0, blank=True, null=True)
    profile                 = models.URLField(blank=True, null=True)
    email                   = models.CharField(max_length=50, blank=True, null=True)
    phone_mobile            = models.CharField(max_length=20, blank=True, null=True)
    phone_home              = models.CharField(max_length=20, blank=True, null=True)
    phone_work              = models.CharField(max_length=20, blank=True, null=True)
    address	                = models.CharField(max_length=256, blank=True, null=True)
    city                    = models.CharField(max_length=50, blank=True, null=True)
    state	                = models.CharField(max_length=50, blank=True, null=True)
    zipcode                 = models.IntegerField(default=0, blank=True, null=True)
    status                  = models.BooleanField(default=False, blank=True, null=True)
    desc                    = models.TextField(blank=True, default=' ')
    addition_info_01        = models.CharField(max_length=50, blank=True, null=True)
    addition_info_02        = models.CharField(max_length=50, blank=True, null=True)
    addition_info_03        = models.CharField(max_length=50, blank=True, null=True)
    is_active               = models.BooleanField(default=True, blank=True, null=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

# ----- Customer and Order -----#

class OrderCatgory(models.Model):
    catname         = models.CharField(max_length=64)
    desc            = models.TextField(blank=True, null=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.catname

# ========================== ORDER ================================ #        

class Order(models.Model):
    orderNumber     = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    customerId      = models.ForeignKey(CustomerCategory, on_delete=models.CASCADE)
    customername    = models.CharField(max_length=70, blank=False, default='')
    Customercount   = models.IntegerField
    payment         = models.DecimalField(max_digits=8, decimal_places=2)
    totalamt        = models.DecimalField(max_digits=8, decimal_places=2)
    empNum          = models.ForeignKey(EmployeeCategory, on_delete=models.CASCADE)
    description     = models.TextField(blank=True, null=True)
    checked         = models.BooleanField(default=False)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.customername

class OrderDetail(models.Model):
    orderMasterId   = models.ForeignKey(Order, on_delete=models.CASCADE)
    image           = models.URLField(blank=True, null=True)
    item            = models.CharField(max_length=70, blank=False, default='')
    author          = models.CharField(max_length=70, blank=False, default='')
    description     = models.TextField(blank=True, null=True)
    published       = models.BooleanField(default=False)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.item

# ---------------------- SECTION ONE RESTAURANTS ----------------------------------------------------------- #


#-------------------------------------RESTAURANT CATEGORY --------------------------------------------------- #
class RestaurantCategory(models.Model):
    # Basic
    restaurant_category    	   = models.CharField(max_length=50, blank=False, null=False, default="")
    phone	   		           = models.CharField(max_length=12, blank=True, null=True, default='')
    email      		           = models.CharField(max_length=50, blank=True, null=True, default='')
        
    # location/contact         
    address			           = models.CharField(max_length=50, blank=True, null=True, default='')
    city                       = models.CharField(max_length=15, blank=True, null=True, default='')
    state                      = models.CharField(max_length=10, blank=True, null=True, default='')
    zipcode                    = models.CharField(max_length=12, blank=True, null=True, default='')
            
    # Photos           
    logo 	 		           = models.URLField(blank=True, null=True)
    profile 	 	           = models.URLField(blank=True, null=True)
        
    # Others           
    is_active                  = models.BooleanField(default=False)
    status                     = models.BooleanField(default=False)
    created_at 		           = models.DateTimeField(auto_now=True)
    updated_at		           = models.DateTimeField(auto_now=True)
    desc                       = models.TextField(blank=True, null=True)

    # Restaurant qs manager
    def __str__(self):
        return self.category
#-------------------------------------CITY and INFORMATION ----------------------------------------------------- #       
class Division(models.Model):
    title        = models.CharField(max_length=128)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)


    def __str__(self):
	    return self.title

    class Meta:
	    ordering = ['title']

    def get_divisions(self):
	    return Division.objects.all()

		

class City(models.Model):
    division        = models.ForeignKey(Division, on_delete=models.CASCADE)
    title           = models.CharField(max_length=128)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)

    def __str__(self):
	    return self.division.title + " - " + self.title
    class Meta:
	    ordering = ['title']

    def get_cities_choice(self):
	    cities  = self.get_cities()
	    choices = []
	    for c in cities:
		    choices.append((c, c))
	    return tuple(choices)
		
    def get_cities(self):
	    citiesObj = City.objects.all()
	    cities    = []
	    for obj in citiesObj:
		    cities.append(obj.title)
	    return cities
#------------------------------------- FOOD -----------------------------------------------------------------        
class FoodCategory(models.Model):
    title	        = models.CharField(max_length=200, blank=False, null=False)
    is_active       = models.BooleanField(default=True, blank=True)
    created_at   	= models.DateTimeField(auto_now=True)
    updated_at		= models.DateTimeField(auto_now=True)

    def __str__(self):
	    return self.title + " - " + "status: " + str(self.is_active)
    class Meta:
	    ordering = ['title']


class Food(models.Model):
	food_category		     = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
	title			         = models.CharField(max_length=512, blank=False, null=False)
	slug                     = models.SlugField(blank=True, unique=True)
	photo    		         = models.URLField(blank=True, null=True)
	key      			     = models.CharField(default='', blank=True, max_length=128)
	price 			         = models.FloatField(default=0.00, blank=True)
	ratio   		         = models.CharField(max_length=50, default='1:1', blank=False, null=False)
	is_active                = models.BooleanField(default=True, blank=True)
	ordered_in_restaurant    = models.IntegerField(default=0, blank=True)
	ordered_in_home    	     = models.IntegerField(default=0, blank=True)
	created_at   	         = models.DateTimeField(auto_now=True)
	updated_at		         = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title



	def get_profile_url(self):
		return reverse('foods:profile', kwargs={'slug':self.slug})
		
	class Meta:
		ordering = ['title']


#------------------------------------- RESTAURANT -----------------------------------------------------------------        
class RestaurantManager(models.Manager):
    def all(self):
        return self.filter(is_active=True)

class Restaurant(models.Model):
    # Basic
    restaurant_category           = models.ForeignKey(RestaurantCategory, on_delete=models.CASCADE, blank=False, null=True)
    title 	    	   = models.CharField(max_length=500, blank=False, null=False)
    slug               = models.SlugField(blank=True, unique=True)
    phone	   		   = models.CharField(max_length=128, blank=False, null=False)
    email      		   = models.CharField(max_length=252, blank=True, null=True, default='')
    # minimum
    min_serve_time     = models.IntegerField(default=30, blank=False, verbose_name='Minimum Serve Time')
    min_order_tk 	   = models.FloatField(default=150.00, blank=False, verbose_name='Minimum Order')
    service_charge     = models.FloatField(default=30.00, blank=False, verbose_name='Service Charge')
    vat_tax            = models.FloatField(default=0.0, blank=True, verbose_name='Vat/Tax')
    # location/contact
    city               = models.ForeignKey(City, on_delete=models.CASCADE)
    address			   = models.CharField(max_length=1024, blank=False, null=False)
    environment		   = models.CharField(max_length=512, blank=False, null=False)
    map_embed_url      = models.TextField(blank=False, default='https://maps.google.com/')
    
    # Photos
    logo 	 		   = models.URLField(blank=True, null=True)
    logo_height_field  = models.IntegerField(default=0)
    logo_width_field   = models.IntegerField(default=0)
    pp    	 		   = models.URLField(blank=True, null=True)
    pp_height_field    = models.IntegerField(default=0)
    pp_width_field     = models.IntegerField(default=0)
  
    # Others
    is_active          = models.BooleanField(default=False)
    is_orderable       = models.BooleanField(default=False)
    created_at 		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)
    extra_info         = models.TextField(blank=True, null=True)
    food_items         = models.ManyToManyField(Food, blank=True)
    # Restaurant qs manager
    objects = RestaurantManager()

    def __str__(self):
        return self.title + " - " + self.slug

    def get_absolute_url(self):
        return reverse("restaurants:detail", kwargs={"slug": self.slug})

    def get_review_page_url(self):
        return reverse("restaurants:review", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-created_at']

class RestaurantReview(models.Model):
    restaurant         = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food               = models.FloatField(default=0.0, blank=True)
    price              = models.FloatField(default=0.0, blank=True)
    service            = models.FloatField(default=0.0, blank=True)
    environment        = models.FloatField(default=0.0, blank=True)
    reviewed_people_no = models.IntegerField(default=0, blank=True)
    average            = models.FloatField(default=0.00, blank=True)
    status             = models.CharField(max_length=50, default='N/A', blank=True, null=True)    
    star1              = models.CharField(max_length=50, default='fa-star-o text-secondary')
    star2              = models.CharField(max_length=50, default='fa-star-o text-secondary')
    star3              = models.CharField(max_length=50, default='fa-star-o text-secondary')
    star4              = models.CharField(max_length=50, default='fa-star-o text-secondary')
    star5              = models.CharField(max_length=50, default='fa-star-o text-secondary')

    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.restaurant.title + ": " + self.status + " - " + str(self.average)

class ServiceTime(models.Model):
    restaurant         = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    open_at            = models.TimeField(blank=True, default='08:00:00')
    close_at           = models.TimeField(blank=True, default='20:00:00')
    saturday           = models.BooleanField(default=True, blank=True)
    sunday             = models.BooleanField(default=True, blank=True)    
    monday             = models.BooleanField(default=True, blank=True)
    tuesday            = models.BooleanField(default=True, blank=True)
    wednesday          = models.BooleanField(default=True, blank=True)
    thursday           = models.BooleanField(default=True, blank=True)
    friday             = models.BooleanField(default=True, blank=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.restaurant.title

def restaurant_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

def restaurant_post_save_receiver(sender, instance, *args, **kwargs):
    qs = RestaurantReview.objects.filter(restaurant=instance)
    if not qs.exists():    
        rr = RestaurantReview()
        rr.restaurant = instance
        rr.save()
    qs = ServiceTime.objects.filter(restaurant=instance)
    if not qs.exists():
        st = ServiceTime()
        st.restaurant = instance
        st.save()

pre_save.connect(restaurant_pre_save_receiver, sender=Restaurant)
post_save.connect(restaurant_post_save_receiver, sender=Restaurant)

#--------------------- NOTIFICATION -------------------------------
class Notification(models.Model):
	account    = models.ForeignKey(User, on_delete=models.CASCADE)
	title 	   = models.CharField(max_length=200, default='', blank=True)
	content    = models.TextField(default='', blank=True)
	link	   = models.TextField(default='')
	created_at		   = models.DateTimeField(auto_now=True)
	updated_at		   = models.DateTimeField(auto_now=True)
	is_seen	   = models.BooleanField(blank=True, null=True)

	def __str__(self):
		return self.account.name + ' - ' + 'seen = ' + str(self.is_seen)

	class Meta:
		ordering = ['-created_at']

#----------------------- ORDERS ----------------------------------------
PAYMENT_METHODS = (
    ('pod', 'Pay On Delivery'),
    ('bkash', 'bKash'),
    ('dbbl', 'DBBL'),
)

DELIVERY_TYPES = (
	('home', 'Home'),
	('hestaurant', 'Restaurant')
)

class Cart(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True)
    key        = models.CharField(max_length=128, blank=True, default='')
    products   = models.ManyToManyField(Food, blank=True)
    quantities = models.CharField(max_length=512, default='', blank=True)
    subtotal   = models.FloatField(default=0.00, blank=True)
    total      = models.FloatField(default=0.00, blank=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)
    is_active  = models.BooleanField(blank=True, null=True)
    def __str__(self):
	    return self.restaurant.title + ' - ' + str(self.total)

class OrderRest(models.Model):
    account             = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    cart                = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    order_id            = models.CharField(blank=True, max_length=256, default='')
    order_no            = models.CharField(blank=True, max_length=256, default='')
    name                = models.CharField(max_length=100, default='', blank=False)
    phone	   	        = models.CharField(max_length=20, default='', blank=False)
    shipping_address    = models.CharField(max_length=200, default='', blank=False)
    status		        = models.BooleanField(default=False, blank=True)
    payment_status      = models.BooleanField(blank=True, null=True)
    shipping_charge     = models.FloatField(default=30.00, blank=True)
    order_type          = models.CharField(max_length=100, default='home', blank=False, choices=DELIVERY_TYPES)
    payment_method      = models.CharField(max_length=100, default="pod", choices=PAYMENT_METHODS)
    expected_time       = models.TimeField(blank=True, null=True, default='')
    discount            = models.FloatField(default=0.00, blank=True)
    cost		        = models.FloatField(default=0.00, blank=True)
    is_active           = models.BooleanField(blank=True, null=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)   
    def get_absolute_url(self):
    	return reverse('orders:detail', kwargs={'order_id': self.order_id})
    
    def __str__(self):
    	return self.name + " - " +  self.phone + " - " + self.shipping_address + " - " + str(self.cost) 
    class Meta:
    	ordering = ['-created_at']

class Discount(models.Model):
    percentage = models.FloatField(default=0.00, blank=True)
    key        = models.CharField(max_length=100, blank=True, default='')
    used       = models.BooleanField(default=False, blank=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return str(self.percentage) + " - " + str(self.used)

# PRE SAVE MODEL STUFFs
def add_key_to_CartObj(sender, instance, *args, **kwargs):
	if not instance.key:
		instance.key = unique_key_generator(instance, size=12)

pre_save.connect(add_key_to_CartObj, sender=Cart)



def add_key_to_DiscountObj(sender, instance, *args, **kwargs):
	if not instance.key:
		instance.key = unique_key_generator(instance, size=randint(6, 10))

pre_save.connect(add_key_to_DiscountObj, sender=Discount)

def add_order_id_to_OrderObj(sender, instance, *args, **kwargs):
	if not instance.order_id:
		instance.order_id = unique_order_id_generator(instance)
	if not instance.order_no:
		instance.order_no = unique_order_no_generator(instance)

pre_save.connect(add_order_id_to_OrderObj, sender=OrderRest)       

#-------------------- PARTNERS --------------------------------------
class PartnerRestaurant(models.Model):
    restaurant 	 	= models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    home_sell_count = models.IntegerField(default=0, blank=True)
    rest_sell_count = models.IntegerField(default=0, blank=True)
    total_sell_tk	= models.FloatField(default=0.0, blank=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)

class Sell(models.Model):
    restaurant    = models.ForeignKey(PartnerRestaurant, on_delete=models.CASCADE)
    foods		  = models.ManyToManyField(Food)
    total_price   = models.FloatField(default=0.0, blank=False, null=False)
    delivery_type = models.CharField(max_length=100, blank=False, null=False)
    destination   = models.CharField(max_length=256, default='', blank=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)
	
#---------------------------- REVIEWS -------------------------------------
class Review(models.Model):
	restaurant  = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	account     = models.ForeignKey(User, on_delete=models.CASCADE)
	title       = models.CharField(max_length=160, default='', blank=False)
	content 	= models.TextField()
	food        = models.IntegerField(default=0, blank=False)
	price       = models.IntegerField(default=0, blank=False)
	service     = models.IntegerField(default=0, blank=False)
	environment = models.IntegerField(default=0, blank=False)
	# (food + price + service + envoronment) / 4.0
	average     = models.FloatField(default=0.0, blank=False)

	star1	    = models.CharField(max_length=50, default='fa-star')
	star2	    = models.CharField(max_length=50, default='fa-star')
	star3	    = models.CharField(max_length=50, default='fa-star')
	star4	    = models.CharField(max_length=50, default='fa-star')
	star5	    = models.CharField(max_length=50, default='fa-star')

	created_at		   = models.DateTimeField(auto_now=True)
	updated_at		   = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.restaurant.title + ": " + self.account.username + " - " + self.title

# ======================== Tutorial ================================ #
class TutorialCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)
    desc = models.TextField(blank=True)
    content = models.TextField(blank=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Tutorial(models.Model):
    tutorial_category = models.ForeignKey(TutorialCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True)
    image = models.URLField(blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
# ========================== Book ==================================#
class BookCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)
    desc = models.TextField(blank=True)
    content = models.TextField(blank=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Book(models.Model):
    book_category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    image = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=70, blank=False, default='')
    author = models.CharField(max_length=70, blank=False, default='')
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# ========================== Blog ==================================#
class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)
    desc = models.TextField(blank=True)
    content = models.TextField(blank=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    image = models.URLField(blank=True, null=True)
    author = models.CharField(max_length=70, blank=False, default='')
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# =================================== CONTACT INFO ========================================== #
class ContactCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)
    desc = models.TextField(blank=True)
    content = models.TextField(blank=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
class Contact(models.Model):
    contact_category   = models.ForeignKey(ContactCategory, on_delete=models.CASCADE)
    first_name       = models.CharField(max_length=100, blank=True, null=True)
    last_name       = models.CharField(max_length=100, blank=True, null=True)
    middle_name       = models.CharField(max_length=100, blank=True, null=True)
    contatct_id = models.CharField(max_length=20, blank=True, null=True)
    gender      = models.CharField(max_length=20, blank=True, null=True)
    age         = models.IntegerField(default=0, blank=True, null=True)
    profile     = models.URLField(blank=True, null=True)
    email       = models.CharField(max_length=50, blank=True, null=True)
    phone_mobile       = models.CharField(max_length=20, blank=True, null=True)
    phone_home       = models.CharField(max_length=20, blank=True, null=True)
    phone_work       = models.CharField(max_length=20, blank=True, null=True)
    address	    = models.CharField(max_length=256, blank=True, null=True)
    city        = models.CharField(max_length=50, blank=True, null=True)
    state	    = models.CharField(max_length=50, blank=True, null=True)
    zipcode     = models.IntegerField(default=0, blank=True, null=True)
    status      = models.BooleanField(default=False, blank=True, null=True)
    desc        = models.TextField(blank=True)
    content     = models.TextField(blank=True)
    addition_info_01        = models.CharField(max_length=50, blank=True, null=True)
    addition_info_02        = models.CharField(max_length=50, blank=True, null=True)
    addition_info_03        = models.CharField(max_length=50, blank=True, null=True)
    is_active   = models.BooleanField(default=True, blank=True, null=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

# =================================== CLIENT INFO ========================================== #
class ClientCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)
    desc = models.TextField(blank=True)
    content = models.TextField(blank=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ClientList(models.Model):
    client_name = models.ForeignKey(ClientCategory, on_delete=models.PROTECT, default="general")
    first_name       = models.CharField(max_length=100, blank=True, null=True)
    last_name       = models.CharField(max_length=100, blank=True, null=True)
    middle_name       = models.CharField(max_length=100, blank=True, null=True)
    contatct_id = models.CharField(max_length=20, blank=True, null=True)
    gender      = models.CharField(max_length=20, blank=True, null=True)
    age         = models.IntegerField(default=0, blank=True, null=True)
    profile     = models.URLField(blank=True, null=True)
    email       = models.CharField(max_length=50, blank=True, null=True)
    phone_mobile       = models.CharField(max_length=20, blank=True, null=True)
    phone_home       = models.CharField(max_length=20, blank=True, null=True)
    phone_work       = models.CharField(max_length=20, blank=True, null=True)
    address	    = models.CharField(max_length=256, blank=True, null=True)
    city        = models.CharField(max_length=50, blank=True, null=True)
    state	    = models.CharField(max_length=50, blank=True, null=True)
    zipcode     = models.IntegerField(default=0, blank=True, null=True)
    status      = models.BooleanField(default=False, blank=True, null=True)
    desc        = models.TextField(blank=True)
    content     = models.TextField(blank=True)
    addition_info_01        = models.TextField(blank=True)
    addition_info_02        = models.TextField(blank=True)
    addition_info_03        = models.TextField(blank=True)
    is_active   = models.BooleanField(default=True, blank=True, null=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

# ==================================== TASK and TASK CATEGORY ========================================= #
class TaskCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)
    desc = models.TextField(blank=True)
    content = models.TextField(blank=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class TaskList(models.Model):
    title = models.CharField(max_length=250)
    task_category = models.ForeignKey(TaskCategory, on_delete=models.PROTECT, default="general")
    desc = models.TextField(blank=True)
    content = models.TextField(blank=True)
    image = models.URLField(blank=True, null=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    scheduled_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    charge = models.DecimalField(max_digits=10, default=0.00, decimal_places=2)
    payment = models.DecimalField(max_digits=10, default=0.00, decimal_places=2)
    balance = models.DecimalField(max_digits=10, default=0.00, decimal_places=2)
    note = models.CharField(max_length=500, default='Hello')
    completed = models.BooleanField(default=False)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# ==================================== PICTURE ========================================= #
class AlbumCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)
    desc = models.TextField(blank=True)
    content = models.TextField(blank=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class AlbumList(models.Model):
    title = models.CharField(max_length=250)
    album_category = models.ForeignKey(TaskCategory, on_delete=models.PROTECT, default="general")
    desc = models.TextField(blank=True)
    content = models.TextField(blank=True)
    image = models.URLField(blank=True, null=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    note = models.CharField(max_length=500, default='Hello')
    completed = models.BooleanField(default=False, blank=True, null=True)
    created_at		   = models.DateTimeField(auto_now=True)
    updated_at		   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


