from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer): 
	
	class Meta:
		model = models.UserProfile 
		fields = ('id', 'email', 'name', 'password') #passing the fields we wanna use in the serializer
		extra_kwargs = {'password': {'write_only': True}} #adding special keyword argument/attribute to the desired fields,so password wont be displayed

	def create(self, validated_data): # To create and return a new User.Special function used to overwrite the create functionality as we wanna be in control of how the users are created.
		user = models.UserProfile(
				email = validated_data['email'],
				name = validated_data['name']
			)
		user.set_password(validated_data['password'])
		user.save()
		return user