import requests
import json
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    print(text)
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    speak('Oh Hello! I am the News Reader Programmed By Krishna. I will read out the latest news for you!')
    speak("How Many News Do You Want to Hear?")
    a = int(input("How Many Latest News do you want to hear?: "))

    # Replace 'YOUR_API_KEY' with your actual News API key
    api_key = 'YOUR_API_KEY'
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        news_data = json.loads(response.text)
        articles = news_data['articles']

        for index, article in enumerate(articles[:a]):  # Loop through the first 'a' articles
            speak(f'''News Number - {index+1}.. 
            Title - {article['title']}
            Description - {article['description']}
            Content - {article['content']}
            ''')

        speak("Thanks For Listening. Come Back Tomorrow For More News...")
    else:
        speak("Unable to fetch news. Please check your API key or network connection.")
