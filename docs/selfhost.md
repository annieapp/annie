# Self Hosting the Backend

One of Annie's cool features is that we allow you to self-host the analytics backend.

## Limitations

Annie requires you to agree to the following terms and limitation before you can download our server:

* Copyright headers MUST be kept.
* You are not allowed to reverse engineer it in any way that can harm the Annie Team or product.
* You MUST keep all privacy protection measures as they are. No modifying them.
* You must follow the terms of [our license](https://github.com/annieapp/annie/blob/master/LICENSE).

## Getting Started

1. You will need to head to the [releases section](https://github.com/annieapp/annie/releases) and download the `annie-server` ZIP or TAR archive.
1. Extract the files from the downloaded archive.
1. You will need to set up WSGI (we have a template in the `wsgi.py` file). We aren't going to explain it here, but once you get it set up and start the server, you should be ready to use the [API](./api.md) on your endpoint URL.
