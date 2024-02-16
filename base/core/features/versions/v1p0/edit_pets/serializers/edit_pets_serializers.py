from rest_framework import serializers
from core.models import Pets
from base.utilities.helpers import validate_birthday
from base.utilities.formatter import CustomDateFormatField

class EditPetsSerializers(serializers.ModelSerializer):
    birthday = CustomDateFormatField(validators=[validate_birthday])
    
    class Meta:
        model = Pets 
        fields = ['name', 'species', 'breed', 'color_or_markings', 'birthday' ,'sex']