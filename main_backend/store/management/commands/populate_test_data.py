from django.core.management.base import BaseCommand
from store.models import Category, Product
from django.contrib.auth import get_user_model
from decimal import Decimal
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate test categories and products'

    def handle(self, *args, **kwargs):
        # Ensure at least one user exists
        user, _ = User.objects.get_or_create(username='testuser', defaults={'email': 'test@example.com'})
        user.set_password('admin123')
        user.save()

        categories = ['Shoes', 'Clothing', 'Accessories']
        for cat in categories:
            category, created = Category.objects.get_or_create(
                name=cat,
                slug=cat.lower().replace(' ', '-'),
                defaults={'created_by': user}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {cat}'))

            # Create 3 products per category
            for i in range(1, 4):
                Product.objects.get_or_create(
                    category=category,
                    title=f'{cat} Product {i}',
                    slug=f'{cat.lower()}-product-{i}',
                    price=Decimal(random.randint(10, 100)),
                    created_by=user,
                )
        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
