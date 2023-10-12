from rest_framework import serializers , validators
from django.contrib.auth.models import User



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username" , "password" , "email" , "first_name" , "last_name"]
        
        extra_kwargs = {
            "password" : {"write_only" : True},
            "email" :{
                "required" : False , 
                "allow_blank" : False,
                "validators" :[
                    validators.UniqueValidator(
                        User.objects.all() , "This email already exist"
                    )
                ]
            }
        }

    def create(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")
        email = validated_data.get("email")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")

        return User.objects.create_user(**validated_data)
