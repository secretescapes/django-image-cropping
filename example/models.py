from django.db import models
from image_cropping.fields import ImageRatioField, ImageCropField, CropForeignKey


class Image(models.Model):
    image_field = ImageCropField(upload_to='image/')
    cropping = ImageRatioField('image_field', '120x100')

    class Meta:
        app_label = 'example'


class ImageFK(models.Model):
    image = CropForeignKey(Image, 'image_field')
    cropping = ImageRatioField('image', '120x100')

    class Meta:
        app_label = 'example'


'''
    feincms example
'''
class ImageContent(Image):
    class Meta:
        app_label = 'example'
        abstract = True


class ImageFKContent(ImageFK):
    class Meta:
        app_label = 'example'
        abstract = True

from feincms.module.page.models import Page
from feincms.content.raw.models import RawContent
Page.register_templates({
    'key': 'base',
    'title': 'Standard template',
    'path': 'base.html',
    'regions': (
        ('main', 'Main content area'),
    ),
})
Page.create_content_type(RawContent)
Page.create_content_type(ImageContent)
Page.create_content_type(ImageFKContent)

