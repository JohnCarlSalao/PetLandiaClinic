from rest_framework import serializers
from core.models import Pets
from base.utilities.helpers import validate_birthday


class EditPetsSerializers(serializers.ModelSerializer):
    birthday = serializers.DateField(validators=[validate_birthday])
    class Meta:
        model = Pets 
        fields = ['name', 'species', 'breed', 'color_or_markings', 'birthday' ,'sex']