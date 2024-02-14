# Plant Database Setup

1. Use the following command to obtain your IP address in Windows PowerShell and then place that IP in the `plantDatabase` settings:

   ```powershell
   (Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias "Wi-Fi").IPAddress


2. In the plantDatabase settings, set the ALLOWED_HOSTS:

ALLOWED_HOSTS = ['192.168.48.26']

3. Additionally, in RetrofitInstance in the Android app (Kotlin) at com.nouman.myapplication2, set the base URL:

.baseUrl("http://192.168.48.26:8000") // with port

4. res -> xml -> security network config -> change IP.

To Run the Django App

Navigate to the Plantdatabase directory and use the following commands in the terminal:

1. Create virtual environment  // if created ignore 
python -m venv venv

2. Activate the virtual environment:
venv/Scripts/Activate

libraries: to install

a.pip install django
python -m django --version
4.2.9

b. pip install tensorflow
pip show tensorflow
Version: 2.15.0
pip uninstall tensorflow

c. pip install numpy
d. python -m pip install Pillow
e. pip install matplotlib
f. pip install  djangorestframework

3. If any changes are made, run this command; otherwise, skip:
python manage.py makemigrations

4. After running the previous command, run this:
python manage.py migrate

5. To start the app:
    python manage.py runserver 192.168.48.26:8000 // place your IP address


Android Studio Version Compatibility

To change in android studio go setting project structure -> project  


Based on:

Android Studio Version	    Required AGP Version
Iguana	                            2023.2.1
Hedgehog	                        2023.1.1
Giraffe	                            2022.3.1
Flamingo	                        2022.2.1
Electric Eel	                    2022.1.1


Plugin Version Compatibility:

Plugin Version	            Minimum Required Gradle Version
8.4 (alpha)	                        8.6-rc-1
8.3 (beta)	                        8.4
8.2	                                8.2
8.1	                                8.0
8.0	                                8.0
7.4	                                7.5

Access Disease Content

Access disease content from https://ausveg.com.au/biosecurity-agrichemical/crop-protection/overview-pests-diseases-disorders/.
