from django.core.management import call_command
from django.test import TestCase


class CloudinaryWagtailAPITestCase(TestCase):
    """
    This tests that the wagtail API displays the image names of images uploaded via 
    CloudinaryField, CloudinaryImageBlock, and snippets via the CloudinarySnippetChooserBlock. 
    In the fixtures, a different image has been uploaded via each of the three ways and this test
    checks for their names in the wagtail api response.
    """

    def setUp(self):
        # wagtailcloudinary assigns a randomized hashed name to images uploaded via wagtail.
        # name of image uploaded via CloudinaryField: av2rxcsuzi1w4dr4fppq
        # name of image uploaded via CloudinaryImageBlock: ccn7ige1z7j6bmnbpsmt
        # name of image uploaded via Snippet: zjqwagpgzppdvoxdssm3
        call_command('loaddata', 'sandbox/foo/tests/test_fixtures.json')

    def test_api(self):
        r = self.client.get('/api/v2/pages/3/?format=json')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'av2rxcsuzi1w4dr4fppq')
        self.assertContains(r, 'ccn7ige1z7j6bmnbpsmt')
        self.assertContains(r, 'zjqwagpgzppdvoxdssm3')