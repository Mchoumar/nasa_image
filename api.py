import requests


def get_api():
    # get the api from the website
    api = "9L8PF7tIHwfSPKk7i8sIj4HgWjCVCU1E7Jsp3H6S"
    url_api = f"https://api.nasa.gov/planetary/apod?api_key={api}"

    # Make request
    url_request = requests.get(url_api)
    # Turn the data into a directory
    url_json = url_request.json()

    # Get the picture from the API
    image = requests.get(url_json["hdurl"])
    image = image.content
    with open("image.jpg", 'wb') as file:
        file.write(image)

    return url_json


if __name__ == "__main__":
    get_api()