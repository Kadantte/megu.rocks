import os
from sanic import Sanic
from sanic import response
import random
import weeb

app = Sanic(__name__)
weebkey = os.environ.get('WEEBSH', None)
assert weebkey
weebsh = weeb.Client(token=weebkey, user_agent="megumin-api")
chants = [
        'Darkness blacker than black and darker than dark, I beseech thee, combine with my deep crimson. The time of awakening cometh. Justice, fallen upon the infallible boundary, appear now as an intangible distortions! I desire for my torrent of power a destructive force: a destructive force without equal! Return all creation to cinders,and come frome the abyss! Explosion!',
	'Oh, blackness shrouded in light, Frenzied blaze clad in night, In the name of the crimson demons, let the collapse of thine origin manifest. Summon before me the root of thy power hidden within the lands of the kingdom of demise Explosion!',
	'Crimson-black blaze, king of myriad worlds, though I promulgate the laws of nature, I am the alias of destruction incarnate in accordance with the principles of all creation. Let the hammer of eternity descend unto me! Explosion!',
	'Crimson-black blaze, king of myriad worlds, though I promulgate the laws of nature, I am the alias of destruction incarnate in accordance with the principles of creation. Let the hammer of eternity descend unto me! ... Burn to ashes within the crimson.',
	'By my efflux of deep crimson, topple this white world!',
	'The tower of rebellion creeps upon man\'s world, The unspoken faith displayed before me, The time has come! Now, awaken from your slumber, and by my madness, be wrought!',
	'Detonation... Detonation... Detonation... Wielder of the most glorious, powerful, and grand explosion magic, My name is Megumin. The blow that I am given to strike turns a blind eye to the fate of my kindred, rendering all hope of rebirth and anguish, and the model by which all forces are judged! Pitiful creature... Synchronize yourself with the red smoke, and atone in a surge of blood!'
        ]

@app.route('/explosion') # EXPLOSION!!!
async def explosion(request):
    image = await weebsh.get_image(imgtype='megumin')
    chant = random.choice(chants)
    return response.json({'chant': chant}) # 'img': image[0]})

if __name__ == '__main__':
    app.run(port=8000)
