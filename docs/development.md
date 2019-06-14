# Developer Docs

Welcome developers, Annie is thrilled to have you.

If you would like to help grow Annie, we love your pull requests.
They mean a lot to us. Here is some general information you may want to know.

## Server

The Annie backend server runs on [Flask](http://flask.pocoo.org/). The source code for that can be found in the `/server` directory.

## Website

The website is split in to 3 different parts.

### Offical Hosted Backend

The official hosted backend ("OHB" for short), is our production instance of Annie.
It is completely free to use, and the platform we suggest you use.
Our hosting provider is [PythonAnywhere](https://pythonanywhere.com).

### Homepage

All the pages on the `www.annieapp.co` domain are hosted on [Netlify](https://netlify.com). The code is located in the `/frontend` directory.

!!! note
    The homepage funs on [Jekyll](https://jekyllrb.com).

### Documentation

The documentation you are reading right now is built with [MkDocs](https://www.mkdocs.org/).
The source is in `/docs` and is hosted by GitHub pages.

## Dependencies

To install all the dependencies you need to run the server, simply open a terminal,
change your working directory to the project root,
and run this command:

```terminal
$ pip install --upgrade --user -r requirements.txt
```

!!! warning
    If you are on Linux or macOS, you may need to add
    `python3 -m` to the beginning of the command for
    it to work. If that doesn't work, try changing
    `pip` to `pip3` and run that.

## Development Server Port

When the Flask development server is turned on, it runs on the selected IP (port 2000).
This can be customized in your `config.py`.
