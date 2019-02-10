from disco.bot import Bot, Plugin
from urllib.parse import urlparse

GREAT_TUNES = 537635615483887667

class YT_Convert(Plugin):
    @Plugin.command('ytmusic', '<url:str>')
    def on_yt(self, event, url):
        try:
            scheme, netloc, path, params, query, fragment = urlparse(url)
            if netloc.lower().endswith("youtube.com"):
                if query.split('&')[0].startswith('v='):
                    result = "**On YT Music:** https://music.youtube.com/watch?{}".format(query.split('&')[0])
                else:
                    result = "Not a video."
            elif netloc.lower().endswith("youtu.be"):
                if len(path) > 3:
                    result = "**On YT Music:** https://music.youtube.com/watch?v={}".format(path[1:])
                else:
                    result = "Uhhh???!"
            else:
                result = "Not a YT link."
        except Exception as e:
            event.msg.reply(str(e))
        else:
            event.msg.reply(result)

    @Plugin.listen('MessageCreate')
    def on_message(self, event):
        if event.message.channel_id == GREAT_TUNES:
            try:
                scheme, netloc, path, params, query, fragment = urlparse(event.message.content)
                if netloc.lower().endswith("youtube.com"):
                    if query.split('&')[0].startswith('v='):
                        result = "**On YT Music:** https://music.youtube.com/watch?{}".format(query.split('&')[0])
                    else:
                        result = False
                elif netloc.lower().endswith("youtu.be"):
                    if len(path) > 3:
                        result = "**On YT Music:** https://music.youtube.com/watch?v={}".format(path[1:])
                    else:
                        result = False
                else:
                    result = False
            except Exception as e:
                print(e)
            else:
                if result:
                    event.reply(result)
