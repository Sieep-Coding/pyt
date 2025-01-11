# Development Tools Using Makefile

I manage the environment through a [makefile,](https://www.gnu.org/software/make/manual/make.html)

View the code [here.](makefile)

> [!CAUTION]  
> Using dev tools incorrectly can cause destruction of your sensitive data. *Use at your own risk.*

# Commands
### Run Local (non-production):
```
make
```
### Run dev environment (non-production):
```
make dev
```
### Run Unit Tests:
```
make test
```
### Run *Production Build*:
> [!TIP]  
> Using this command will build an executable *and* run it.
```
make build
```
### Cleanup local files:
> [!CAUTION]  
> You will lose your data.
```
make fresh
```
### Cleanup build files:
> [!CAUTION]  
> You will lose your data.
```
make freshbuild
```
### Initialize database only:
```
make db
```
### Create a new database backup:
> [!TIP]  
> Using this command will copy your database to folder `backup/`
```
make backup
```