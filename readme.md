
# spark - *S*ystem for *P*rogressive and *A*ctive *R*elationship *K*eeping

[![wakatime](https://wakatime.com/badge/user/2156ce13-ae9d-4c0e-a543-89b2bddcd2f6/project/5ede5fcd-c567-4543-9b11-5abcf126f720.svg)](https://wakatime.com/badge/user/2156ce13-ae9d-4c0e-a543-89b2bddcd2f6/project/5ede5fcd-c567-4543-9b11-5abcf126f720)

A `Python` GUI to manage essential business data with `tkinter` and a *FAST* `SQLite` backend.

I created this for myself but you are welcome to use it yourself under the [MIT License.](LICENSE)

> [!WARNING]  
> Not ready for a production enviroment (yet). *Use at your own risk.*

## Manage Contacts, Projects, and more.
![](https://github.com/Sieep-Coding/pyt/blob/main/assets/image.png)

## Core Features
I want this to run as fast as possible, with the goal of keeping the executable under a few hundred MB.
Some other features include:
- Adding, managing, removing data through forms
- Exporting to common filetypes
- Viewing data and reports easily
- *Fast AF* `SQLite` backend
- [Hot reloading](hot_reload.py) for insane productivity.

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

#### But why?
> "In the same way a woodworker invests the time in a jig, a programmer can build a code generator. 
> Once built, it can be used throughout the life of the project at virtually no cost."
> -- [*Andrew Hunt*](https://en.wikipedia.org/wiki/Andy_Hunt_(author))