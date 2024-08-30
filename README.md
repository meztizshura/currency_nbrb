
# currency_nbrb
Module fetches currency nbrb

This module uses api to get the rate of the Belarusian ruble against foreign currencies
# Adm Odoo Compose

### Before run project prepare odoo_pg_pass string and config/odoo.conf:
```
cp odoo_pg_pass.example odoo_pg_pass
cp config/odoo.conf.example config/odoo.conf
```

### To create a key, go to Settings>Technical>System Parameters create a new key with a value
```
key: nbrb_api_url
value: https://api.nbrb.by/exrates/rates
```



