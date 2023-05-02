from django.db import models

# Create your models here.
# cutomer table
class customers(models.Model):
    # name column with maxmimum length of 255
    name = models.CharField(max_length=255)
    # email column with maximum length of 255
    email = models.CharField(max_length=255)
    # phone no column with max_length of 20
    phone_no = models.CharField(max_length=20)

# orders table
class orders(models.Model):
    # customerid column with integer data type and primary key
    customer_id = models.IntegerField(null=False,primary_key=True),
    #  total_price column of float field
    total_price = models.FloatField(null=False,max_length=10)
    #  timestamp field for created_at 
    created_at = models.DateTimeField(auto_now_add=True,null=False)
    # foreign key relationship betweem orders and customers table
    fk_orders_customers= models.ForeignKey(customers,on_delete=models.CASCADE)

# products table
class products(models.Model):
    # name column with maximum length of 255
    name= models.CharField(max_length=255)
    # price column with maximum length of 10 and numeric type
    price = models.FloatField(max_length=10)