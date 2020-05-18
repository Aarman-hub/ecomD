from django.db import models

# Create your models here.


class Category(models.Model):
	STATUS = (
			('True','Publish'),
			('False','Draft'),
		)
	parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	keywords = models.CharField(max_length=255)
	description = models.CharField(max_length=250)
	image = models.ImageField(blank=True, null=True, upload_to='category/')

	status = models.CharField(max_length=30, choices=STATUS)

	slug = models.SlugField()

	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.title


class Product(models.Model):
	STATUS= (
		('True','Publish'),
		('False','Draft'),
		)

	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	keywords = models.CharField(max_length=255)
	description =models.CharField(max_length=200)
	images = models.ImageField(null=True, blank=True, upload_to='product/')
	price=models.FloatField()
	amount=models.IntegerField()
	minamount=models.IntegerField()
	#detail=RichTextUploadingField()
	detail=models.TextField()
	status=models.CharField(max_length=10, choices=STATUS)
	create_at=models.DateTimeField(auto_now_add=True)
	upload_to=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

