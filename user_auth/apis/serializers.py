from rrf import serializers
from rrf.exeptions import ValidationError
from rrf.authentications import get_token_by_user
from django.contrib.auth import get_user_model

User = get_user_model()


class GetTokens :

    @property
    def tokens(self) : 
        token = get_token_by_user(self.user)
        return {
            'token' : token
        }


class LoginSerializer (serializers.Serializer, GetTokens):
    email:str
    password:str

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError(message='invalid email')
        
        if not user.check_password(password) : 
            raise ValidationError(message='invalid password')
        
        self.user = user


class RegisterSerialier (serializers.ModelSerializer, GetTokens) : 
    class Meta:
        model = User
        fields = ['username','email','password']

    def validate(self, attrs) -> dict:
        username = attrs['username']
        email = attrs['email']

        if User.objects.filter(username=username).exists() : 
            raise ValidationError(message='username already exists, try another one')
        
        if User.objects.filter(email=email).exists() : 
            raise ValidationError(message='email already exists, try another one')
        
    def save(self):
        user = User.objects.create_user(**self.validated_data)
        self.user = user
        return user
     