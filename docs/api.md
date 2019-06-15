# API

The Annie API has a whole set of features. This page documents them.

!!! note
    This page shows the latest documentation for the latest features.
    Features implemented in later versions then what you may have
    can be documented here.

The official hosted API base is `https://api.annieapp.co/`.
If you are [self hosting](./selfhost.md), your base will be different, but the commands below should be the same.

## New Key

To generate a new key, you can visit `/keys/new`. It will return a JSON payload like this if it worked:

```json
{ 'result': { 'fail': false, 'auth': { 'key': 'somekey', 'private-key': 'someotherkey' } } }
```

!!! warning
    Keep your generated keys safe,
    you won't be able to see them
    again!

## Usage Statistics

To get how many users Annie has logged join requests for, you can use the `/stats.json?key=YOUR_ANNIE_PUBLIC_KEY&private=YOUR_ANNIE_PRIVATE_KEY` endpoint.

If you don't have a public/private key set to get stats from, see the `New Key` section above.

It should return a payload like this if it worked:

```json
{ 'result': { 'fail': false, 'connections': 'COUNT' } }
```

Note that `COUNT` will be an integer.
