from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestBackend():

    def __init__( self ):
        return

    def setUp(self):        # create user
        self.auth_user = AuthUser.objects.create_user(USERNAME, password=PASSWORD)
        self.cam_user = AuthUserExtension(user=self.auth_user, tour_complete=1)
        self.cam_user.save()
        self.client = Client()
        self.response = HttpResponse
        self.request = HttpRequest

    def test_login(self):
        # create and submit a form
        self.response = self.client.post('/members/login',
                {'username':USERNAME, 'password':PASSWORD})
        self.assertRedirects(self.response, '/system/profile')

    def tearDown(self):
        AuthUserExtension.objects.filter(user=self.auth_user).delete()
        AuthUser.objects.filter(username=USERNAME).delete()

    def myTest(self):
        driver = webdriver.Firefox()
        # driver.manage().window().maximize()

        driver.get("https://cam2.ecn.purdue.edu/members/login?next=/system/submissions")

        assert "CAM" in (driver.title)
        username = driver.find_element_by_name('username')
        username.send_keys("apoorvvw")
        password = driver.find_element_by_name('password')
        password.send_keys("test123")

        try: 
            password.send_keys(Keys.RETURN)
        except:
            raise ValueError
            print("Page not found")

        #continue_link = driver.find_element_by_partial_link_text('/system/submissions')

        my_submission = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/ul/li[5]/a")
        my_submission.send_keys(Keys.RETURN)
        #elem.send_keys("pycon")
        #elem.send_keys(Keys.RETURN)
        #assert "No results found." not in driver.page_source

        #driver.close()

    if __name__ == '__main__':
        t = TestBackend
        t.setUp();
        t.myTest();
        t.tearDown();

