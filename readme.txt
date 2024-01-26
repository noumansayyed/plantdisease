#########

1. Use the following command to obtain your IP address in windows powershell and then place that IP in the plantDatabase settings:

(Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias "Wi-Fi").IPAddress

##########

2.In the plantDatabase settings, set the ALLOWED_HOSTS:

ALLOWED_HOSTS = ['192.168.48.26']

3. Additionally, in RetrofitInstance in the Android app (Kotlin) at com.nouman.myapplication2, set the base URL:

.baseUrl("http://192.168.48.26:8000") // with port


4. Specify the models' paths in the plantapp views:  // django

if it correct dont do any thing

MODELS = {
    "potato": {
        "model": "model_Potato/1",  # change over here in views
        "class_names": ["Potato Early blight", "Potato Late blight", "Potato Healthy"]
    },
    "tomato": {
        "model": "model_tomato/1",
        "class_names": ['Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight','Tomato_Leaf_Mold', 'Tomato__Tomato_mosaic_virus', 'Tomato_healthy']
    },
}




To run the Django app, navigate to the Plantdatabase directory and use the following commands in the terminal:



1. env/Scripts/Activate // to start the virtual environment


libraries: to install

a.pip install django
b. pip install tensorflow
c. pip install numpy
d. python -m pip install Pillow
e. pip install matplotlib
f. pip install  djangorestframework

this all are required install only once 


2. If any changes are made, run this command; otherwise, skip: python manage.py makemigrations
3. After running the previous command, run this: python manage.py migrate

######

4. To start the app: python manage.py runserver 192.168.48.26:8000 // place your IP address

######

Enable Developer Options on your Android device:

Open the "Settings" app on your Android device.
Scroll down and select "About phone" or "About device."
Find the "Build number" entry and tap it seven times to enable Developer Options. You may need to enter your device's unlock code or PIN.


Once Developer Options is activated, go back to the main "Settings" screen.
Scroll down and select "Developer options."
Toggle the switch for "USB debugging" to enable it.
Connect your Android device to your computer:

Use a USB cable to connect your Android device to your computer.

Run your Android application on the device:

Open your integrated development environment (IDE) like Android Studio.
Build and run your application, selecting your connected Android device as the deployment target.

#####

Access disease content from "https://ausveg.com.au/biosecurity-agrichemical/crop-protection/overview-pests-diseases-disorders/".