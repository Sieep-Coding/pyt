# Development Tools Using Makefile

> [!CAUTION]  
> Using dev tools incorrectly can cause destruction of your data. *Use at your own risk.*

### Run Local (non-production):
```
make
```
### Run dev environment (non-production):
```
make dev
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