from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)
		#strip to get rid of the /n (new line whitespace ) that django 
		#adds to the template at the end of the file after </html> 

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'Post'
		request.POST['item_text'] = 'A new list item'

		response = home_page(request)
		self.assertIn('A new list item', response.content.decode())
		expected_html = render_to_string(
			'home.html',
			{'new_item_test': 'A new list item'}
			)
		self.assertEqual(response.content.decode(), expected_html)


