from disco.bot import Bot, Plugin
import rolldice


class TestPlugin(Plugin):
    @Plugin.command('roll', '<dice:str> [comment:str...]')
    def on_roll(self, event, dice, comment=''):
        try:
            result, explanation = rolldice.roll_dice(dice)
        except rolldice.DiceGroupException as e:
            event.msg.reply(str(e))
        except rolldice.DiceOperatorException as e:
            event.msg.reply(str(e))
        except Exception as e:
            event.msg.reply(str(e))
        else:
            if comment:
                event.msg.reply(
                    '{} rolled *{}* \n **{}** \t`{}`'.format(str(event.msg.author)[:-5], comment, result, explanation))
            else:
                event.msg.reply(
                    '{} rolled a dice! \n **{}** \t`{}`'.format(str(event.msg.author)[:-5], result, explanation))
