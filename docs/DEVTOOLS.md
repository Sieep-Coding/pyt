# Development Tools Using Makefile

> [!CAUTION]  
> Using dev tools incorrectly can cause destruction of your sensitive data. *Use at your own risk.*

I manage the environment through a [makefile,](https://www.gnu.org/software/make/manual/make.html)

View the code [here.](makefile)

## Quickstart

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `make install`            | Installs dependencies                            |
| `make`                    | Run Local                                        |
| `make dev`                | Run Dev Environment                              |
| `make backup`             | Backup database/flat data files.                 |

# Commands
### Run Local (non-production):
```bash
make install #install requirements.txt
make
```
### Run dev environment (non-production):
```bash
make dev
```
### Run Unit Tests:
```
make test
```
### Run *Production Build*:
> [!TIP]  
> Using this command will build an executable *and* run it.
```bash
make build
```
### Cleanup local files:
> [!CAUTION]  
> You will lose your data.
```bash
make fresh
```
### Cleanup build files:
> [!CAUTION]  
> You will lose your data.
```bash
make freshbuild
```
### Initialize database only:
```bash
make db
```
### Create a new database backup:
> [!TIP]  
> Using this command will copy your database to folder `backup/`
```bash
make backup
```