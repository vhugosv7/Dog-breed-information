# Dog-breed-information
Flask app to generate a specific number of random dog images and show some interesting information for each breed. For this project, I'm using the DOG API to return random dog images. To see DOG API documentation, please visit its website: https://dog.ceo/dog-api/documentation/random.


## Features

- **Generating a specific number of random dog images**: The `random_dogBreed` function allows you to generate a specific number of random dog images and view each image to download. The number of images ranges from 1 to a maximum of 50 images.
- **View specific information by each dog breed.**: The `breeds()` function displays some information by dog breed when the user select a specific dog breed.
- **All dogs breed information.**: The `info_dogs.py` contains a dictionary where all the dog breeds information is stored and used in the `breeds()` function.


## Installation

Follow the steps below to set up and run this project locally.

### Prerequisites

- Flask 3.1.0
- requests 2.32.3
- substring 0.2
- Python 3.11.7
- Bootstrap 5.02

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/vhugosv7/Dog-breed-information.git

2. Navigate to the project folder:
   ```bash
   cd Dog-breed-information

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Flask application:
   ```bash
   python main_menu.py

5. Open your browser and navigate to http://127.0.0.1:5000/ to interact with the application.


### Screnshoots


* **Requesting 5 random images**
  
![Random images]![image](https://github.com/user-attachments/assets/1c03fcf7-b6b9-4b46-a5dc-827862ffd88e)


* **View random dog image**
  
  ![View image]![image](https://github.com/user-attachments/assets/41fb287b-cddc-47bd-bd9c-da7e03836b0b)


* **List of dog breeds**
  
  ![Dog list]![image](https://github.com/user-attachments/assets/a6ae8256-465c-462f-9c36-c026d20c645c)


* **Detailed information by breed**
  
  ![Dog details]![image](https://github.com/user-attachments/assets/71c3bea1-9efd-4bb3-85bf-5fc8328bb059)
 
  (Available to download as PDF file)

* **PDF with the selected dog breed**
  
  ![PDF file]![image](https://github.com/user-attachments/assets/6f90918c-3d16-4132-a675-98a18809a920)


