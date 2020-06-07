# -*- coding: utf-8 -*-
import os
import unittest

from flask import Flask
from flaskext.autoversion import Autoversion

class AutoversionTestCase(unittest.TestCase):

	def setUp(self):
		app = Flask(__name__, static_url_path='/tests/static/')
		app.autoversion = True
		self.av = Autoversion(app)
		self.app = app

	def tearDown(self):
		self.app = None
		self.av = None

	def test_00_existing_file(self):
		filename = 'app.css'
		fullpath = os.path.join('tests/static/', filename)
		timestamp = str(os.path.getmtime(fullpath))
		with self.app.app_context(), self.app.test_request_context(base_url='http://localhost'):
			versioned_path = self.av.static_autoversion(filename)
			assert versioned_path.endswith(timestamp)

	def test_01_nonexisting_file(self):
		filename = 'nothere.css'
		with self.app.app_context(), self.app.test_request_context(base_url='http://localhost'):
			versioned_path = self.av.static_autoversion(filename)
			assert versioned_path.endswith(filename)