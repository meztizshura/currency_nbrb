
# currency_nbrb
Module fetches currency nbrb
# Adm Odoo Compose

## Before run project prepare odoo_pg_pass string and config/odoo.conf:
```
cp odoo_pg_pass.example odoo_pg_pass
cp config/odoo.conf.example config/odoo.conf
```

## Install python requirements
There are some modules that include requirements.txt files. Make sure you install them before launching any adm_<module_name> module.
To install all the requirements execute the following command after the odoo app is run:
```
make req
```
