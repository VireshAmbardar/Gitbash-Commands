import requests
from flask import Flask , render_template, request , url_for
from geopy.geocoders import Nominatim
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/weather",methods=["GET","POST"])
def weatheras():
    if request.method=="POST":
        location = request.form["location"]
        print(location)
        #return render_template("weather.html",location=location)
        geolocator = Nominatim(user_agent="my_app")
        try:
            l_rain=url_for('static',filename='light_rain.jpg')
            b_rain=url_for('static',filename='broken_cloud.jpg')
            f_rain=url_for('static',filename='few_cloud.jpg')
            s_rain=url_for('static',filename='scattered.jpg')
            m_rain=url_for('static',filename='moderate_rain.jpg')
            c_rain=url_for('static',filename='clear_rain.jpg')


            loc = geolocator.geocode(location)
            latitude = loc.latitude
            longitude = loc.longitude
            print(f"Latitude: {latitude}, Longitude: {longitude}")
            v=f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid=dc67e5d1431c8414a23b4f3e212f9c89"
            response = requests.get(v)
            data=response.json()
            lis=data["list"]
            w1=[]
            t1=[]
            r1=[]
            for weather_data in lis:
                w1.append(weather_data['dt_txt'])
                t1.append(round(weather_data['main']['temp']-273.15))
                r1.append(weather_data['weather'][0]['description'])
            return render_template("weather.html", w1=w1, t1=t1, r1=r1, location=location, latitude=latitude, longitude=longitude, l_rain=l_rain, b_rain=b_rain, f_rain=f_rain, s_rain=s_rain,c_rain=c_rain,m_rain=m_rain)


            #return render_template("weather.html",w1=w1,t1=t1,r1=r1,location=location,latitude=latitude, longitude=longitude)
        except AttributeError:
            print("Location not found.")
        

        # v="https://api.openweathermap.org/data/2.5/forecast?lat=21.7679&lon=78.8718&appid=dc67e5d1431c8414a23b4f3e212f9c89"
        # response = requests.get(v)

        # data=response.json()
        

        # lis=data["list"]
        # w1=[]
        # t1=[]
        # r1=[]
        # for weather_data in lis:
        #     w1.append(weather_data['dt_txt'])
        #     t1.append(round(weather_data['main']['temp']-273.15))
        #     r1.append(weather_data['weather'][0]['description'])

            # print(f"{weather_data['dt_txt']}")
            # print(f" temparute is {round(weather_data['main']['temp']-273.15)} C")
            # print(f"weather desc {weather_data['weather'][0]['description']}")
            
        



if __name__ == '__main__':
    app.run(debug=True)
