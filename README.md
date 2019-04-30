# Restrict_API
An api in which a user can't access another users data/profile. Ex:~ user with profile id 7 should be able to access /api/profile/7/ but not /api/profile/8/

# Some Features of this API

* Custom User Model :- using email for login instead of username.
* TokenAuthentication
* A MessageViewSet which has just a list to explain the objective of this API.
* A user can create an account using this api and can only access his own data by accessing his user id endpoint. For ex:~ api/profile/2 