# API

The Annie API has a whole set of features. This page documents them.

!!! note
    This page shows the latest documentation for the latest features.
    Features implemented in later versions then what you may have
    can be documented here.

The hosted API base is `https://api.annieapp.co/`.

## New Key

To generate a new key, you can visit `/keys/new`. It will return a JSON payload like this if it worked:

```json
{'result': { 'fail': false, 'auth': { 'key': 'somekey', 'private-key': 'someotherkey' }, 'message': 'you are now ready to use the Annie API' } }
```

!!! warning
    Keep your generated keys safe,
    you won't be able to see them
    again!
