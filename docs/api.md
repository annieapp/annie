# API

The Annie API has a whole set of features. This page documents them.

!!! note
    This page shows the latest documentation for the latest features.
    Features implemented in later versions then what you may have
    can be documented here.

The official hosted API base is `https://api.annieapp.co/`.
If you are [self hosting](./selfhost.md), your base will be different, but the commands below should be the same.

## Common Response

All of our JSON endpoints return this at the very least:

```json
{ "result": { "fail": false } }
```

or if it did fail:

```json
{ "result": { "fail": true } }
```

This can help for easily determining if something worked or not!

## New Key

To generate a new key, you can visit `/keys/new`. It will return a JSON payload like this if it worked:

```json
{ "result": { "fail": false, "auth": { "key": "somekey", "private-key": "someotherkey" } } }
```

!!! warning
    Keep your generated keys safe,
    you won't be able to see them
    again!

## Delete a Key

If you want to erase a key, visit `/keys/delete?key=ANNIE_PUBLIC_KEY&private=ANNIE_PRIVATE_KEY`.

It will return a JSON payload like the common response success if it worked.

!!! warning
    You can't reverse this once done.

## Log a "use" or "page visit"

To get Annie to increase the number for 'joins' as they will be called here, you can use the `/connect?key=ANNIE_PUBLIC_KEY` endpoint.

If you don't have a public/private key set to get stats from, see the `New Key` section above.

If all is well, a payload like the common response success will be sent back.

Simple as that!

## Usage Statistics

To get how many users Annie has logged join requests for, you can use the `/stats.json?key=YOUR_ANNIE_PUBLIC_KEY&private=YOUR_ANNIE_PRIVATE_KEY` endpoint.

If you don't have a public/private key set to get stats from, see the `New Key` section above.

It should return a payload like this if it worked:

```json
{ "result": { "fail": false, "connections": "COUNT", "last-join": "SomeDateAndTime" } }
```

Note that `COUNT` will be an integer, but is a string just so docs will show the code block.
As for the `"last-join"` element, it will tell you of the most *recent* join request.
