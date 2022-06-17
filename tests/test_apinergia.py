#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests.exceptions import HTTPError
from unittest import TestCase

from somenergia_apinergia.apinergia import Apinergia, Authentication

class TestApinergia(TestCase):

    @classmethod
    def setUpClass(cls):
        from dotenv import load_dotenv   #for python-dotenv method
        load_dotenv(dotenv_path='.env.test', override=True)                    #for python-dotenv method

        import os

        cls.username = os.environ.get('USERNAME')
        cls.password = os.environ.get('PASSWORD')
        cls.base_url = os.environ.get('BASEURL')
        cls.contractid = os.environ.get('CONTRACTID')

        Authentication.set_url(cls.base_url)

        cls.token = Authentication().get_token(cls.username, cls.password)

        cls.api = Apinergia(cls.base_url, cls.username, cls.password)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__auth__base(self):
        token = Authentication().get_token(self.username, self.password)

        self.assertTrue(token)
        self.assertEqual(token, self.token)

    def test__auth__badauth(self):
        with self.assertRaises(HTTPError) as e:
            Authentication().get_token('m.rajoy', 'fakepassword')
        self.assertEqual(401, e.exception.response.status_code)

    def test__get_cch_curves__base(self):

        # cch_types = ['tg_cchval','tg_cchautoconsum','tg_gennetabeta']
        cch_type   = 'tg_cchval'
        start_date = '2022-01-01'
        end_date   = '2022-02-01'

        result = self.api.get_cch_curves(self.contractid, cch_type, start_date, end_date)

        expected_keys = ['contractId', 'meteringPointId', 'measurements']
        expected_measurement = {
            'season': 0,
            'ai': 209,
            'ao': 0,
            'date': '2021-12-31 22:00:00+0000',
            'dateDownload': '2022-01-04 02:43:43',
            'dateUpdate': '2022-01-04 02:43:43'
        }
        self.assertTrue(result)
        self.assertListEqual(list(result[0].keys()), expected_keys)
        self.assertDictEqual(result[0]['measurements'], expected_measurement)

    def test__get_cch_curves__unauth(self):
        # cch_types = ['tg_cchval','tg_cchautoconsum','tg_gennetabeta']
        cch_type   = 'tg_cchval'
        start_date = '2022-01-01'
        end_date   = '2022-02-01'

        result = self.api.get_cch_curves(self.contractid, cch_type, start_date, end_date)

        expected_keys = ['contractId', 'meteringPointId', 'measurements']
        expected_measurement = {
            'season': 0,
            'ai': 209,
            'ao': 0,
            'date': '2021-12-31 22:00:00+0000',
            'dateDownload': '2022-01-04 02:43:43',
            'dateUpdate': '2022-01-04 02:43:43'
        }
        self.assertTrue(result)
        self.assertListEqual(list(result[0].keys()), expected_keys)
        self.assertDictEqual(result[0]['measurements'], expected_measurement)


# vim: ts=4 sw=4 et