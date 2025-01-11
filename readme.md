# spark - *S*ystem for *P*rogressive and *A*ctive *R*elationship *K*eeping

[![wakatime](https://wakatime.com/badge/user/2156ce13-ae9d-4c0e-a543-89b2bddcd2f6/project/5ede5fcd-c567-4543-9b11-5abcf126f720.svg)](https://wakatime.com/badge/user/2156ce13-ae9d-4c0e-a543-89b2bddcd2f6/project/5ede5fcd-c567-4543-9b11-5abcf126f720)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

<img src="https://github.com/Sieep-Coding/pyt/blob/main/assets/p.png"
     alt="Spark Logo"
     style="float: left; margin-right: 10px;" 
     width=180px
     />

A `Python` GUI to manage essential business data with `tkinter` and a *FAST* `SQLite` backend.

> [!WARNING]  
> Not ready for a production environment (yet). *Use at your own risk.*

## Manage Contacts, Projects, and more.
![](https://github.com/Sieep-Coding/pyt/blob/main/assets/image.png)

## Core Features
I want this to run as fast as possible, with the goal of keeping the executable under a few hundred MB.

Some other features include:
- **Adding, managing, removing data** through forms.
- **No server!** Uses a single `.db` file locally. 
- **Exporting** to common file-types.
- **Viewing data, reports, table relationships** easily.
- **Simple, *Fast AF***, `SQLite` backend.
- [Hot reloading](hot_reload.py) with [watchdog](https://pypi.org/project/watchdog/) for insane productivity.

## Navigation
- [Frontend](frontend/gui.py)
- [Backend](backend/database.py)
- [Dev docs](docs/DEVTOOLS.md)
- [Dev tools](makefile)

## Dependencies

> [!IMPORTANT]  
> Only tested on Linux so far!

- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Sun Valley Theme](https://github.com/rdbende/Sun-Valley-ttk-theme/tree/main)
- [Sqlite](https://www.sqlite.org/)

![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

#### But why?
> "In the same way a woodworker invests the time in a jig, a programmer can build a code generator. 
> Once built, it can be used throughout the life of the project at virtually no cost."
> -- [*Andrew Hunt*](https://en.wikipedia.org/wiki/Andy_Hunt_(author))