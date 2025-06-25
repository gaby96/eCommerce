from django.core.management.base import BaseCommand
from store.models import Category, Product, Album
from django.contrib.auth import get_user_model
from decimal import Decimal
from django.core.files import File
from PIL import Image
from io import BytesIO
import os

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate test categories, products, and images'

    def handle(self, *args, **kwargs):
        user, _ = User.objects.get_or_create(username='testuser', defaults={'email': 'test@example.com'})
        user.set_password('admin123')
        user.save()

        sample_image_path = os.path.join('media', 'test_images', 'sample.jpg')
        if not os.path.exists(sample_image_path):
            self.stdout.write(self.style.WARNING(f"Image not found: {sample_image_path}"))
            return

        categories = ['Shoes', 'Clothing', 'Accessories']
        for cat in categories:
            category, _ = Category.objects.get_or_create(
                name=cat,
                slug=cat.lower().replace(' ', '-'),
                defaults={'created_by': user}
            )

            for i in range(1, 4):
                product, _ = Product.objects.get_or_create(
                    category=category,
                    title=f'{cat} Product {i}',
                    slug=f'{cat.lower()}-product-{i}',
                    price=Decimal(i * 10),
                    created_by=user,
                )

                # Add image if none exist
                if not product.images.exists():
                    with open(sample_image_path, 'rb') as img_file:
                        image_file = File(img_file, name=f'{product.slug}.jpg')
                        Album.objects.create(
                            image=image_file,
                            created_by=user,
                            content_object=product
                        )

        self.stdout.write(self.style.SUCCESS("Test products with images added."))
