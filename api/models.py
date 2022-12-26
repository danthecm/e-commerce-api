from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
# SKU --> stock keeping unit
# 

def category_image_path(instance, filename):
    return "category/icons/{}/{}".format(instance.name, filename)


def product_image_path(instance, filename):
    return "product/images/{}/{}".format(instance.title, filename)


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True



class Size(BaseModel):
	size 					= models.CharField(max_length=20, null=False)
	slug 					= models.SlugField(max_length=150, unique=True, null=True, blank=True)

	def __str__(self):
		return str(self.size)

# M:M --> product:Category
class Category(models.Model):
	name 					= models.CharField(max_length=60,unique=True,
							 verbose_name="category_name",
							help_text="format: required, max-100")
	slug 					= models.SlugField(max_length=150, unique=True, null=True)
	icon 					= models.ImageField(upload_to=category_image_path, blank=True)
	is_active 				= models.BooleanField(default=False)
	created 				= models.DateTimeField(auto_now_add=True)
	modified 				= models.DateTimeField(auto_now=True)


	def __str__(self):
		return str(self.name)

#
# 1:M --> product:subproduct, # M:M --> product:Category
class Product(models.Model):  
	name 					= models.CharField(max_length=60, null=False)
	type 					= models.CharField(max_length=60, null=True, blank=True)
	description 			= models.CharField(max_length=250, blank=True)
	created_at 				= models.DateTimeField(auto_now_add=True)
	updated_at 				= models.DateTimeField(auto_now=True)
	categories 				= models.ManyToManyField(Category, blank=True)
	slug 					= models.SlugField(max_length=150, unique=True, null=True)
	
	def __str__(self):
		return str(self.name)

# M:1 --> subproduct:product, 1:M --> subproduct:size, 1:M -> subproduct:Brand'
class SubProduct(models.Model): 
	name 					= models.CharField(max_length=60, null=False)
	SKU 					= models.AutoField(primary_key=True, null=False)
	store_price 			= models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
	retail_price 			= models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
	sale_price 				= models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
	in_stock 				= models.BooleanField(default=False)
	weight 					= models.IntegerField(null=True, default=1)
	type 					= models.CharField(max_length=20, null=False)
	size					= models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
	created_at 				= models.DateTimeField(auto_now_add=True)
	updated_at 				= models.DateTimeField(auto_now=True)
	product 				= models.ForeignKey(Product, on_delete=models.CASCADE)
	slug 					= models.SlugField(max_length=150, unique=True, null=True)
	quantity 				= models.IntegerField(default=1)

	def __str__(self):
		return str(self.name)



class WeightUnit(models.Model):
	name 					= models.CharField(max_length=60)
	abbreviation 			= models.CharField(max_length=10)
	default 				= models.IntegerField(default=0)
	subproduct 				= models.ForeignKey(SubProduct, on_delete=models.CASCADE, related_name="weight_unit_sub")
	slug 					= models.SlugField(max_length=150, unique=True, null=True)

	def __str__(self):
		return self.sub_product

class Brand(models.Model):
	name 					= models.CharField(max_length=60)
	slug 					= models.SlugField(max_length=150, unique=True, null=True)
	subproduct 				= models.ForeignKey(SubProduct, on_delete=models.CASCADE, related_name="brand_sub")

	def __str__(self):
		return str(self.name)

	

# 1:M --> subproduct:colour
class Colour(models.Model):
	colour 					= models.CharField(max_length=20, null=False)
	slug 					= models.SlugField(max_length=150, unique=True, null=True)
	subproduct 				= models.ForeignKey(SubProduct, on_delete=models.CASCADE)

	def __str__(self):
		return self.sub_product



class ProductType(models.Model):
	name 					= models.CharField(max_length=60, null=True, verbose_name="type_name")
	product 				= models.ForeignKey(Product, on_delete=models.CASCADE)
	slug 					= models.SlugField(max_length=150, unique=True, null=True)

	def __str__(self):
		return "%s %s" % (self.name, self.product)



# M:1 --> Media:subproduct
class Media(models.Model):
	title 					= models.CharField(max_length=60, null=False)
	description 			= models.TextField(max_length=60, null=True, blank=True)
	alt_text 				= models.TextField(max_length=60, null=True)
	image 					= models.ImageField(upload_to=product_image_path, blank=True)
	subproduct				= models.ForeignKey(SubProduct, on_delete=models.CASCADE)
	slug 					= models.SlugField(max_length=150, unique=True, null=True)
	
	def __str__(self):
		return str(self.title)


class Stock(models.Model):
	last_checked 			= models.DateTimeField(auto_now=True)
	units 					= models.CharField(max_length=60)
	units_sold 				= models.CharField(max_length=60)
	slug 					= models.SlugField(max_length=150, unique=True, null=True)
	subproduct				= models.ForeignKey(SubProduct, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.sub_product
