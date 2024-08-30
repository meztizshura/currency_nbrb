import os
from datetime import datetime
from http.client import responses
from logging import getLogger
import requests
from odoo import models


logger = getLogger(__name__)


class FetchCurrencyModel(models.TransientModel):
    _name = 'currency_nbrb.fetch_currency'
    _description = 'Fetch Currency from nbrb'

    def fetch_currency(self):
        api_url = self.env['ir.config_parameter'].sudo().get_param('nbrb_api_url')
        active_currencies = self.env['res.currency'].search([
            ('active', '=', True),
        ])
        current_company = self.env.user.company_id
        user_currency = self.env.user.currency_id

        rate = requests.get(api_url + "/" + user_currency.name, params={
            'periodicity': 0,
            'parammode': 2,
        })
        rate_data = rate.json()
        for currency in active_currencies:
            response = requests.get(api_url + "/" + currency.name, params={
                'periodicity': 0,
                'parammode': 2,
            })
            data = response.json()

            currency_rate = data.get('Cur_OfficialRate', 1)
            currency_scale = data.get('Cur_Scale', 1)
            rate_to_byn = rate_data.get('Cur_OfficialRate', 1) / rate_data.get('Cur_Scale', 1)
            value = (currency_rate / currency_scale) / rate_to_byn
            existing_rate = self.env['res.currency.rate'].search([
                ('name', '=', datetime.today()),
                ('currency_id', '=', currency.id),
                ('company_id', '=', current_company.id)
            ])

            if existing_rate:
                existing_rate.write({
                    'inverse_company_rate': value,
                })
            else:
                self.env['res.currency.rate'].create({
                    'currency_id': currency.id,
                    'name': datetime.today(),
                    'inverse_company_rate': value,
                })
