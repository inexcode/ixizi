# ixizi
Our homegrown discord bot plugins for [disco](https://github.com/b1naryth1ef/disco)

# Usage
Add some of our plugins to your `plugins` directory. You may use `config.json` as a reference.

To launch the bot use something like
```bash
python3.6 -m disco.cli --config /path/to/config.json
```

# Plugins in this repo
## coffee (in russian)
Chooses the drink from Coffee Like menu. Or something from Nescafe. Uses py-rolldice as a randomizer.

## dicer
Just a wrapper for the [py-rolldice](https://github.com/ThePlasmaRailgun/py-rolldice) library.

## references
Fetches Firebase to show the reference card. Make sure to configure this one.
It uses the following structure:
```
references
 +-- object_id
 |   +-- color [integer]
 |   +-- description
 |   +-- image [URL]
 |   +-- name
 |   +-- owner
 |   +-- ownerAvatar [URL]
 |   +-- thumbnail
```

## ytconvert
Just converts Youtube links to Youtube music links.
All Youtube links in `GREAT_TUNES` channel will be converted automatically.

---

Licensed under WTFPL.
Inex Code.
