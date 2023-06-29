from django.core.files import File
from django.db.models import ImageField
from io import BytesIO
import requests


class FileOrURLImageField(ImageField):
    def to_python(self, value):
        if not value:
            return value

        if hasattr(value, 'read'):
            # If the value has a 'read' method, it is a file-like object (e.g., file upload)
            return value

        if value.startswith('http://') or value.startswith('https://'):
            # If the value starts with 'http://' or 'https://', treat it as a URL and download the file
            response = requests.get(value)
            response.raise_for_status()
            file_name = value.split('/')[-1]
            file_content = response.content
            file = BytesIO(file_content)
            file_wrapper = File(file, name=file_name)
            return file_wrapper

        # Otherwise, the value is likely a file path
        return super().to_python(value)
