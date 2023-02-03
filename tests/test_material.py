from odoo.tests import common

class MaterialTestCase(common.TransactionCase):
	def setUp(self):
		super(MaterialTestCase, self).setUp()
		self.data = self.env['material.data']

	def test_material_code(self):
		test_one = self.data.create({
			'material_code'	: 'AAA-001',
			'material_name'	: 'Jeans suka saya',
			'tipe'			: 'jeans',
			'price'			: 100000,
			'supplier'		: 'PT. Azka Muhammad'
		})

		test_two = self.data.create({
			'material_code'	: 'AAA-002',
			'material_name'	: 'Jeans suka saya',
			'tipe'			: 'jeans',
			'price'			: 100000,
			'supplier'		: 'PT. Azka Muhammad'
		})

		self.assertTrue(test_one.material_code != test_two.material_code)
		self.assertFalse(test_one.material_code == test_two.material_code)

		print("Material code test is successful")

	def test_price(self):
		test_three = self.data.create({
			'material_code'	: 'AAA-003',
			'material_name'	: 'Jeans suka saya',
			'tipe'			: 'jeans',
			'price'			: 100000,
			'supplier'		: 'PT. Azka Muhammad'
		})

		self.assertTrue(test_three.price >= 100)
		self.assertTrue(isinstance(test_three.harga, int))

		self.assertFalse(test_three.price < 100)
		self.assertFalse(isinstance(test_three.harga, float))
		self.assertFalse(isinstance(test_three.harga, str))

		print("Price test is successful")

	def test_tipe(self):
		test_four = self.data.create({
			'material_code'	: 'AAA-004',
			'material_name'	: 'Jeans suka saya',
			'tipe'			: 'jeans',
			'price'			: 100000,
			'supplier'		: 'PT. Azka Muhammad'
		})

		self.assertTrue(test_four.tipe in ['fabric', 'jeans', 'cotton'])
		self.assertFalse(test_four.tipe not in ['fabric', 'jeans', 'cotton'])

		print("Material type test is successful")
