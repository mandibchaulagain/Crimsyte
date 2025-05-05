from django.db import models

class Vendor(models.Model):
    """Model to represent a vendor"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    featured = models.BooleanField(default=False)
    website = models.URLField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    """Model to represent an event"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    contact_email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    """Model to represent an image in the gallery"""
    image = models.ImageField(upload_to='gallery_images/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Image {self.id}"

class ContactMessage(models.Model):
    """Model to represent a contact form submission"""
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name} on {self.submitted_at}"
