from django.db import models
class book_management(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    isbn=models.CharField(max_length=100)
    current_status=models.DateTimeField(auto_now_add=True)
    barrowing_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (self.author)

class patron_management(models.Model):
    author =models.ForeignKey(book_management,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    contact=models.IntegerField()
    membership_details=models.CharField(max_length=100)
    card_number=models.IntegerField()
    due_date=models.DateTimeField(auto_now_add= True )
    def __str__(self) -> str:
        return f"{self.name}"
class book_borroewing(models.Model):
    author=models.ForeignKey(book_management,on_delete=models.CASCADE)
    name=models.ForeignKey(patron_management,on_delete=models.CASCADE)
    borrowing_date=models.DateTimeField(auto_now_add=True)
    retun_date=models.DateTimeField()
    def __str__(self) -> str:
        return f'{self.author}==>{self.name}==>{self.borrowing_date}'