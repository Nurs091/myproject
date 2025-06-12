# # myapp/serializers.py
# from rest_framework import serializers
# from .models import Ad, Category, AdImage, AdStatus, AdHistory, User

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'


# class AdStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdStatus
#         fields = '__all__'


# class AdImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdImage
#         fields = ['id', 'image']


# class AdSerializer(serializers.ModelSerializer):
#     images = AdImageSerializer(many=True, read_only=True)
#     status = AdStatusSerializer(read_only=True)
#     category = CategorySerializer(read_only=True)

#     class Meta:
#         model = Ad
#         fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'phone']

# # 🔐 РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ С EMAIL-КОДОМ
# # class RegisterSerializer(serializers.ModelSerializer):
# #     phone = serializers.CharField(required=True)

# #     class Meta:
# #         model = User
# #         fields = ('username', 'email', 'password', 'phone')
# #         extra_kwargs = {'password': {'write_only': True}}

# #     def validate_phone(self, value):
# #         if not value:
# #             raise serializers.ValidationError("Поле 'phone' обязательно.")
# #         return value

# #     def create(self, validated_data):
# #         user = User.objects.create_user(
# #             username=validated_data['username'],
# #             email=validated_data['email'],
# #             phone=validated_data['phone'],  # обязательно
# #             password=validated_data['password'],
# #             is_active=False
# #         )
# #         code = EmailVerification.generate_code()
# #         EmailVerification.objects.create(email=user.email, code=code)
# #         send_verification_code(user.email, code)
# #         return user


# # ✅ ПОДТВЕРЖДЕНИЕ КОДА
# # class VerifyEmailSerializer(serializers.Serializer):
# #     email = serializers.EmailField()
# #     code = serializers.CharField(max_length=6)
