from disco.bot import Bot, Plugin
from disco.types.message import MessageEmbed
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Auth
cred = credentials.Certificate('firebase-key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://<your-project-id>.firebaseio.com'
})


class RefPlugin(Plugin):
    @Plugin.command('ref', '<character:str>')
    def on_red(self, event, character):
        try:
            dbref = db.reference('references/{}'.format(character.lower()))
            data = dbref.get()
            if data:
                embed = MessageEmbed()
                embed.set_author(name=data.get('owner', 'Unknown owner'), url=data.get('ownerURL'), icon_url=data.get('ownerAvatar'))
                embed.title = data.get('name', 'Unnamed')
                if data.get('description'):
                    embed.description = data['description']
                embed.color = data['color']
                if data.get('image'):
                    embed.set_image(url=data['image'])
                if data.get('thumbnail'):
                    embed.set_thumbnail(url=data['thumbnail'])
                event.msg.reply(embed=embed)
            else:
                event.msg.reply("Not found")
        except Exception as e:
            event.msg.reply(str(e))
