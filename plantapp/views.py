from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Leaf
from .serializers import LeafSerializer
from .models import UserRegister
from .serializers import UserRegisterSerializer

from .models import Disease
from .serializers import DiseaseSerializer

from django.http import JsonResponse
from django.views import View
from .models import PlantImage

import numpy as np
from io import BytesIO
from PIL import Image

import tensorflow as tf

from rest_framework.views import APIView

MODELS = {
    "potato": {
        "model": "model_Potato/1",
        "class_names": ["Potato Early blight", "Potato Late blight", "Potato Healthy"]
    },
    # "guava": {
    #     "model": "model_guava/pretrain_model.h5",
    #     "class_names": ['Canker', 'Dot', 'Healthy', 'Mummification', 'Rust']
    # },
    "tomato": {
        "model": "model_Tomato/1",
        "class_names": ['Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight','Tomato_Leaf_Mold', 'Tomato__Tomato_mosaic_virus', 'Tomato_healthy']
    },
}

 

@api_view(['POST'])
def create_leaf(request):
    serializer = LeafSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def leaf_data_view(request):
    leaves = Leaf.objects.all()
    UserRegisters = UserRegister.objects.all()
    plant_images = PlantImage.objects.all()  # Retrieve all PlantImage data

    return render(request, 'leaf_data.html', {'leaves': leaves, 'UserRegisters': UserRegisters, 'plant_images': plant_images})


@api_view(['POST'])
def register_user(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User registered successfully', 'uniqueId': user.uniqueId}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email:
        return Response({"error": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)
    if not password:
        return Response({"error": "Password is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = UserRegister.objects.get(email=email)
        if user.password != password:
            return Response({"error": "Invalid password."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = UserRegisterSerializer(user)
        return Response(serializer.data)
    except UserRegister.DoesNotExist:
        return Response({"error": "Invalid email."}, status=status.HTTP_401_UNAUTHORIZED)
    



# @api_view(['POST'])
# def predict_disease(request):
#     file_fields = request.FILES.keys()
#     print(f"Fields present: {list(file_fields)}")
    
#     def read_file_as_image(data) -> np.ndarray:
#         image = np.array(Image.open(BytesIO(data)))
#         return image
    
#     if 'image' in request.FILES:
#         image_file = request.FILES['image']
        
#         # Accessing details of the uploaded file
#         file_name = image_file.name
#         file_size = image_file.size
#         file_content_type = image_file.content_type
        
#         image = read_file_as_image(image_file.read())
        
#         img_batch = np.expand_dims(image, 0)
#         predictions = {}
#         for model_name, model_data in MODELS.items():
#             model_path = model_data["model"]
#             class_names = model_data["class_names"]

#             model = tf.keras.models.load_model(model_path)
#             prediction = model.predict(img_batch)

#             predictions[model_name] = {
#                 "prediction": prediction,
#                 "class_name": class_names[np.argmax(prediction)],
#                 "confidence": np.max(prediction)
#             }

#         print(predictions)
        
#         # Find the class with the highest confidence among both potato and tomato predictions
#         highest_confidence_prediction = max(predictions.values(), key=lambda x: x["confidence"])

#         # Round the confidence value after determining the highest confidence prediction
#         highest_confidence_prediction["confidence"] = round(highest_confidence_prediction["confidence"] * 100, 2)
        
#         # Define the confidence threshold
#         confidence_threshold = 85  # You can adjust this threshold
        
#         if highest_confidence_prediction["confidence"] < confidence_threshold:
#             final_prediction = {
#                 "class_name": "Unknown",
#                 "confidence": highest_confidence_prediction["confidence"]
#             }
#         else:
#             final_prediction = {
#                 "class_name": highest_confidence_prediction["class_name"],
#                 "confidence": highest_confidence_prediction["confidence"]
#             }
                
#         print(f"Uploaded file details - Name: {file_name}, Size: {file_size}, Content Type: {file_content_type}")
        
#         return Response(final_prediction, status=status.HTTP_200_OK)
#     else:
#         return Response({'error': 'No image found in request'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def predict_disease(request):
    file_fields = request.FILES.keys()
    print(f"Fields present: {list(file_fields)}")
    
    def read_file_as_image(data) -> np.ndarray:
        image = np.array(Image.open(BytesIO(data)))
        return image
    
    if 'image' in request.FILES:
        image_file = request.FILES['image']
        
        # Accessing details of the uploaded file
        file_name = image_file.name
        file_size = image_file.size
        file_content_type = image_file.content_type
        
        image = read_file_as_image(image_file.read())
        
        img_batch = np.expand_dims(image, 0)
        
        # Load the single disease prediction model
        model_path = "best_model.h5"
        class_names = ["Apple Black Rot", "Apple Healthy", "Apple Scab","Cedar Apple Rust", "Pepper Bacterial Spot", "Pepper Healthy", "Potato Early Blight", "Potato Healthy", "Potato Late Blight", "Tomato Bacterial Spot", "Tomato Healthy", "Tomato Septoria Leaf Spot", "Tomato Yellow Leaf Curl Virus"]  # Adjust based on your class names
        model = tf.keras.models.load_model(model_path)
        
        # Make a prediction using the loaded model
        prediction = model.predict(img_batch)

        final_prediction = {
            "class_name": class_names[np.argmax(prediction)],
            "confidence": np.max(prediction) * 100
        }
        
        print(f"Uploaded file details - Name: {file_name}, Size: {file_size}, Content Type: {file_content_type}")
        
        return Response(final_prediction, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'No image found in request'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def disease_detail(request, id):
    disease = Disease.objects.get(pk=id)
    serializer = DiseaseSerializer(disease)
    return Response(serializer.data)

class GetUserInfo(APIView):
    def get(self, request, unique_id):
        try:
            user = UserRegister.objects.get(uniqueId=unique_id)
            serializer = UserRegisterSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserRegister.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        

from django.shortcuts import get_object_or_404

class UpdateUserInfo(APIView):
    def post(self, request, unique_id):
        user = get_object_or_404(UserRegister, uniqueId=unique_id)
        serializer = UserRegisterSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            if request.data: 
                serializer.save(update_fields=['name', 'email'])
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

