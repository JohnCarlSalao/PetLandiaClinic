from rest_framework import serializers
from petlandia.models import Pets
from petlandia.utils.helpers import validate_birthday
class CreatePetsSerializers(serializers.ModelSerializer):
    birthday = serializers.DateField(validators=[validate_birthday])
    class Meta:
        model = Pets 
        fields = ['name', 'species', 'breed', 'color_or_markings', 'birthday' ,'sex']