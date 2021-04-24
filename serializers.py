class Users(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = '__all__'  
        
class Ads(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = '__all__'  
        
        
class Images(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'  
        
