from rest_framework import serializers 
from tutorials.models import Tutorial,Bookings
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id','name',
                  'photo_url',)

class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bookings
        fields = ('id','booking_time',)