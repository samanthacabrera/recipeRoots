from models import *
from services import *


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()

#  jeff = User(
#         username = "Jeff",
#         email = "jeff@email.com",
#         password = "hellothere",
#         icon = "image@url.com"
#     )
#     bezos = User(
#         username = "Bezos",
#         email = "bezos@email.com",
#         password = "yeet",
#         icon = "hmmm@url.com"
#     )
#     elon = User(
#         username = "Elon",
#         email = "elon@email.com",
#         password = "hellothere",
#         icon = "image@url.com"
#     )
#     musk = User(
#         username = "Musk",
#         email = "musk@email.com",
#         password = "yeet",
#         icon = "hmmm@url.com"
#     )
#     andrew = User(
#         username = "Andrew",
#         email = "andrew@email.com",
#         password = "hellothere",
#         icon = "image@url.com"
#     )
#     tristan = User(
#         username = "Tristan",
#         email = "tristan@email.com",
#         password = "yeet",
#         icon = "hmmm@url.com"
#     )
#     tate = User(
#         username = "Tate",
#         email = "tate@email.com",
#         password = "hellothere",
#         icon = "image@url.com"
#     )
#     mark = User(
#         username = "Mark",
#         email = "mark@email.com",
#         password = "yeet",
#         icon = "hmmm@url.com"
#     )
#     bill = User(
#         username = "Bill",
#         email = "bill@email.com",
#         password = "hellothere",
#         icon = "image@url.com"
#     )
#     gates = User(
#         username = "Gates",
#         email = "gates@email.com",
#         password = "yeet",
#         icon = "hmmm@url.com"
#     )
#     db.session.add_all([jeff, bezos, elon, musk, andrew, tristan, tate, mark, bill, gates])
#     db.session.commit()

#     denver = Marker(
#         caption = "This city sucks",
#         image_url = "https://marvel-b1-cdn.bc0a.com/f00000000295839/red.msudenver.edu/wp-content/uploads/2022/02/denversummer_hero2_RED.jpg",
#         latitude = 39.7392,
#         longitude = -104.9903,
#         user_id = 1
#     )
#     london = Marker(
#         caption = "Got stabbed here",
#         image_url = "https://assets.editorial.aetnd.com/uploads/2019/03/topic-london-gettyimages-760251843-feature.jpg",
#         latitude = 51.5074,
#         longitude = -0.1278,
#         user_id = 4
#     )
#     rome = Marker(
#         caption = "Great Pizza",
#         image_url = "https://www.fodors.com/wp-content/uploads/2018/10/HERO_UltimateRome_Hero_shutterstock789412159.jpg",
#         latitude = 41.9028,
#         longitude = 12.4964,
#         user_id = 3
#     )
#     moscow = Marker(
#         caption = "блять",
#         image_url = "https://www.nationsonline.org/gallery/Russia/State-Historical-Museum-Moscow.jpg",
#         latitude = 55.7558,
#         longitude = 37.6173,
#         user_id = 4
#     )
#     sydney = Marker(
#         caption = "ǝʇɐɯ ᴉO",
#         image_url = "https://i.natgeofe.com/n/bd48279e-be5a-4f28-9551-5cb917c6766e/GettyImages-103455489cropped.jpg",
#         latitude = -33.8688,
#         longitude = 151.2093,
#         user_id = 9
#     )
#     vancouver = Marker(
#         caption = "Opioid capital of Canada",
#         image_url = "https://upload.wikimedia.org/wikipedia/commons/5/57/Concord_Pacific_Master_Plan_Area.jpg",
#         latitude = 49.2827,
#         longitude = -123.1207,
#         user_id = 6
#     )
#     dubai = Marker(
#         caption = "What color is your Bugatti?",
#         image_url = "https://miro.medium.com/v2/resize:fit:1358/1*sf4nQKh1ArnsfbT1uFly4w.jpeg",
#         latitude = 25.276987,
#         longitude = 55.296249,
#         user_id = 7
#     )
#     new_york = Marker(
#     caption="The city that never sleeps",
#     image_url="https://www.nycgo.com/images/made/1.-Jin-Joo-Kim_600_399_70.jpg",
#     latitude=40.7128,
#     longitude=-74.0060,
#     user_id=2
#     )
#     tokyo = Marker(
#     caption="Land of the Rising Sun",
#     image_url="https://www.japan.travel/content/dam/nto/en/images/experience/attractions/guides/culture-and-heritage/001_top/001_main/001_main.jpg",
#     latitude=35.6895,
#     longitude=139.6917,
#     user_id=8
#     )
#     berlin = Marker(
#     caption="Capital of Germany",
#     image_url="https://cdn.getyourguide.com/img/location/5ffebf4ba07fb.jpeg/99.jpg",
#     latitude=52.5200,
#     longitude=13.4050,
#     user_id=10
#     )
#     toronto = Marker(
#     caption="The Six",
#     image_url="https://media.tacdn.com/media/attractions-splice-spp-674x446/0a/99/a6/22.jpg",
#     latitude=43.651070,
#     longitude=-79.347015,
#     user_id=11
#     )
#     beijing = Marker(
#     caption="Capital of China",
#     image_url="https://www.travelchinaguide.com/images/city/beijing/beijing.jpg",
#     latitude=39.9042,
#     longitude=116.4074,
#     user_id=12
#     )
#     rio_de_janeiro = Marker(
#     caption="Carnival Capital",
#     image_url="https://media.timeout.com/images/105211701/image.jpg",
#     latitude=-22.9068,
#     longitude=-43.1729,
#     user_id=13
#     )
#     cape_town = Marker(
#     caption="Mother City",
#     image_url="https://cdn.britannica.com/69/195669-050-535A27B4/Table-Mountain-Cape-Town-South-Africa.jpg",
#     latitude=-33.9249,
#     longitude=18.4241,
#     user_id=14
#     )
#     bangkok = Marker(
#     caption="City of Angels",
#     image_url="https://www.bangkok.com/info/images/bangkok-highlights.jpg",
#     latitude=13.7563,
#     longitude=100.5018,
#     user_id=15
#     )
   