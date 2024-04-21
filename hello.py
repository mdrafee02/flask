from flask import Flask, render_template

app = Flask(__name__)

# Sample JSON data
data = [
    {
        "user_profile_image": "https://th.bing.com/th/id/OIP.IGNf7GuQaCqz_RPq5wCkPgAAAA?rs=1&pid=ImgDetMain",
        "name": "John Doe",
        "sub_title": "Web Developer",
        "text": "proficient in Python, MySql, Django.",
        "feed_image": "https://media.licdn.com/dms/image/sync/D4E10AQHu5je8O74QkA/image-shrink_800/0/1712563159008/397854452_120201158055470711_1902635828166285340_njpg?e=1713967200&v=beta&t=cc-kekepz7WWTdEoroZbzjjVMC-iyLwoAnpOlogcsAY"
    },
    
    {
        "user_profile_image": "https://www.ninjaonlinedating.com/blog/wp-content/uploads/2019/08/SmileModifiedKRAK.jpg",
        "name": "Jane Smith",
        "sub_title": "Graphic Designer",
        "text": "looking for a graphic designer role",
        "feed_image": "https://media.licdn.com/dms/image/D4D22AQH755izVuMUcw/feedshare-shrink_2048_1536/0/1713019650654?e=1716422400&v=beta&t=FWwUdrxSb2Q8v6xYunV7JZw6sAvU81ddsvm89eQBj6o"
    }
]

@app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
