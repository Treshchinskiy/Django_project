from django.db import models


class TextRequest(models.Model):
    input_text=models.CharField(max_length=300)
    output_text=models.CharField(max_length=300)
    
    def __str__(self):
        return self.input_text
    
    
    
class Test(models.Model):
    name=models.CharField(max_length=100)
    article=models.CharField(max_length=1000)