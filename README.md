resume
======

Python resume generator. From YAML to PDF and static HTML.

Installing
----------

    https://bitbucket.org/kciarnie/resume
    cd resume
    python setup.py develop

Usage
-----

1. Look at resume examples in the `resumes` folder and create your own.
2. Edit `config.make` and update it with your settings.
3. Run `make` to build HTML and PDF files that will go to the `build` directory.


### PDF

To just create PDF file:

    make pdf

### Publishing

To publish html on your server via SSH, edit `RSYNC_LOCATION` in `config.make` and run:

    make publish


License
-------
[MIT License](https://bitbucket.org/kciarnie/resume/LICENSE)
