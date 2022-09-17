from django.db import models


class LibraryUser(models.Model):

    username = models.CharField(max_length = 20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobilenumber = models.IntegerField()
    email = models.CharField(max_length= 20)

    def __str__(self):
        return self.username



class Book(models.Model):
    book_id = models.IntegerField(primary_key=True,unique=True,null=False)
    book_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    stock_quantity = models.IntegerField(blank=True)
    created = models.DateField(blank=True)
    modified = models.DateField(auto_now_add=True)
    language = models.CharField (max_length =10, blank=True)
    
    def __str__(self):
        return self.book_name

    

    




