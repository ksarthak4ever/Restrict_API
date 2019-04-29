from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserProfileManager(BaseUserManager): #Used to tell django how to use our custom user model.
	
	def create_user(self,email,name,password=None): #creates a new user profile object.
		if not email:
			raise ValueError('Users must have an email address.')

		email = self.normalize_email(email) #to normalize entered email i.e all characters to lowercase 
		user = self.model(email=email, name=name)

		user.set_password(password) #set_password will encrypt the password in a hash
		user.save(using=self._db)

		return user

	def create_superuser(self,email,name,password): #to create and save a new superuser with given details
		user = self.create_user(email, name, password)
		user.is_superuser = True
		user.is_staff = True
		user.save(using = self._db)
		return user


class UserProfile(AbstractBaseUser, PermissionsMixin): #That is actually creating User using this Class,Used to represent a user profile inside our system or overwrite the existing user model made by django as in our api we want user to login through emails
	email = models.EmailField(max_length=200, unique=True)
	name = models.CharField(max_length=200)
	is_active = models.BooleanField(default=True) 
	is_staff = models.BooleanField(default=False) 

	objects = UserProfileManager() 

	USERNAME_FIELD = 'email' #this field is used for login
	REQUIRED_FIELDS = ['name']

	def get_full_name(self): #to get a user full name by the django admin 
		return self.name

	def __str__(self): #to make email object readable. 
		return self.email