#Installing Flask

_$ pip install Flask_

    Flask supports Python 3.4 and newer, Python 2.7
    
    Dependencies
    These distributions will be installed automatically when installing Flask.
    
        Werkzeug implements WSGI, the standard Python interface between applications and servers.
        Jinja is a template language that renders the pages your application serves.
        MarkupSafe comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.
        ItsDangerous securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.
        Click is a framework for writing command line applications. It provides the flask command and allows adding custom management commands.
        
     
    Virtual environments
    Use a virtual environment to manage the dependencies for your project, both in development and in production.
    
    WSGI - Web Server Gateway Interface 