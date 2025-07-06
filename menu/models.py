from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('appetizer', 'مقبلات'),
        ('main', 'الوجبات الرئيسية'),
        ('dessert', 'حلويات'),
        ('drink', 'مشروبات'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name