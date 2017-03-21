resume
======

Python resume generator. From YAML to PDF and static HTML.

Installing
----------

    git clone https://github.com/kciarnie/resume
    cd resume
    make html

Usage
-----

1. Look at resume examples in the `resumes` folder and create your own.
2. Edit `Makefile` and update it with your settings. Specifically `resumes/kevin.yaml` to your yaml file
3. Run `make html` to build HTML and PDF files that will go to the `build` directory.


### PDF

To just create PDF file:

    make pdf

### Publishing

To publish html on your server via SSH, type 

    make html

Just make sure you set your BUILD_DIR in the `Makefile`

License
-------
[MIT License](https://bitbucket.org/kciarnie/resume/LICENSE)