from django.db import models


class Processes(models.Model):
    timestamp = models.DateTimeField()
    cursor_coordinates = models.CharField(max_length=50)
    image_data_source = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"Event at {self.timestamp} - Cursor: {self.cursor_coordinates} | Image Source: {self.image_data_source}"
