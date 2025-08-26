from flask import Flask, render_template, request
import requests
from info_dogs import get_breed_details
import substring

# Change the template folder path, according to your path.
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])  # Main Route
def random_dogBreed():
    #   Initialize Final_result with a default value
    Final_result = []
    #  List to store the breeds from the Final_result variable
    list_breeds = []
    if request.method == 'POST':
        try:
            # Get the number of images requested. Ex: 10
            imgs_number = int(request.form['search'])
            # Getting multiple random images from all dogs collection
            url2 = f"https://dog.ceo/api/breeds/image/random/{imgs_number}"
            # Request in json format
            json_data = requests.get(url2).json()
            # Getting value of 'message'
            Final_result = json_data['message']

            #  Formatting the dog's breed name
            for row in Final_result:
                '''Extract the dog breed without all the default name
                Ex:images.dog.ceo/breeds/australian-kelpie/IMG_2599.jpg"'''
                breed_card_title = substring.substringByChar(
                    row[30:], startChar=row[30:][0], endChar="/")
                # Append each breed in the list without the "/"
                list_breeds.append(breed_card_title[:-1])

        #  Catching exceptions
        except Exception as e:
            print("Error:", e)
            Final_result = []

    return render_template('main.html', Final_result=Final_result,
                           list_breeds=list_breeds)


@app.route('/dog-details/', methods=['GET', 'POST'])
def breeds():
    # Breed list
    breeds = "https://dog.ceo/api/breeds/list/all"
    json_data_breeds = requests.get(breeds).json()
    Final_result_breeds = json_data_breeds['message']
    #  These lines are for testing
    '''print("THI IS BREEDS", Final_result_breeds)
    print(type(Final_result_breeds), "!!TYPE!!")'''
    user_selected = ""
    breed_selected = "Select breed"
    breed_selected_info = {}

    if request.method == 'POST':
        try:
            # Breed select from dropdown list
            user_selected = request.form['selected_user_breed']
            # Getting the image requested by the user
            link_breed = f"https://dog.ceo/api/breed/{user_selected}/images/random"
            #  Request method from the DOG.CEO API
            json_data_breed_choosed = requests.get(link_breed).json()
            # Geting the link of the image
            breed_selected = json_data_breed_choosed['message']
            # Returning all the details from the breed selected by the user
            breed_selected_info = get_breed_details(user_selected)

        except Exception as e:
            print(e)
            return render_template('main.html')

    return render_template('dog-details.html',
                           Final_result_breeds=Final_result_breeds,
                           breed_selected=breed_selected,
                           user_selected=user_selected,
                           breed_selected_info=breed_selected_info)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
