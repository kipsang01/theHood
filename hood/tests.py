from django.test import TestCase
from .models import HoodMember,Neighborhood,Service,Post,Review
from django.contrib.auth.models import User
# Create your tests here.
class NeighboardTestClass(TestCase):
    def setUp(self):
         self.user1 = User(username='psang',first_name='Enock',last_name ='kipsang',email='psang254@gmail.com',password ='sjsiuwueufbccn')
         self.hood1 = Neighborhood(name='runda',location ='nairobi', creator = self.user1,profile_pic ='picture')
         self.post1 = Post(content = 'good hood',author = self.user1,neighborhood = self.hood1)
         self.member1 = HoodMember(member = self.user1, hood =self.hood1)
         
         
    def test_instance(self):
        self.assertTrue(isinstance(self.user1,User))
        self.assertTrue(isinstance(self.hood1,Neighborhood))
        self.assertTrue(isinstance(self.post1,Post))
        self.assertTrue(isinstance(self.member1,HoodMember))