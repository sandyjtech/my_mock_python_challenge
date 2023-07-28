import unittest

from social_network import User, SocialNetwork, UserProfile

class TestSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.network = SocialNetwork()
        self.user1 = User(1, "Alice")
        self.user2 = User(2, "Bob")
        self.user3 = User(3, "Charlie")

        self.profile1 = UserProfile(1, "Alice", 28, "New York")
        self.profile2 = UserProfile(2, "Bob", 25, "San Francisco")
        self.profile3 = UserProfile(3, "Charlie", 30, "Los Angeles")

    def test_add_user(self):
        self.network.add_user(self.user1)
        self.network.add_user(self.user2)

        self.assertIn(self.user1, self.network.users)
        self.assertIn(self.user2, self.network.users)

    def test_get_user_by_id(self):
        self.network.add_user(self.user1)

        retrieved_user = self.network.get_user_by_id(1)
        self.assertEqual(retrieved_user, self.user1)

        non_existent_user = self.network.get_user_by_id(999)
        self.assertIsNone(non_existent_user)

    def test_add_friend(self):
        self.network.add_user(self.user1)
        self.network.add_user(self.user2)

        self.user1.add_friend(self.user2)

        self.assertIn(self.user2, self.user1.friends)
        self.assertIn(self.user1, self.user2.friends)

    def test_get_common_friends(self):
        self.network.add_user(self.user1)
        self.network.add_user(self.user2)
        self.network.add_user(self.user3)

        self.user1.add_friend(self.user2)
        self.user1.add_friend(self.user3)
        self.user2.add_friend(self.user3)

        common_friends = self.network.get_common_friends(self.user1, self.user2)
        self.assertEqual(common_friends, [self.user3])

    def test_get_mutual_friends(self):
        self.network.add_user(self.user1)
        self.network.add_user(self.user2)
        self.network.add_user(self.user3)

        self.user1.add_friend(self.user2)
        self.user1.add_friend(self.user3)
        self.user2.add_friend(self.user3)

        mutual_friends = self.network.get_mutual_friends(self.user1, self.user2)
        self.assertEqual(mutual_friends, [self.user3])

    def test_get_friends_of_friends(self):
        self.network.add_user(self.user1)
        self.network.add_user(self.user2)
        self.network.add_user(self.user3)

        self.user1.add_friend(self.user2)
        self.user2.add_friend(self.user3)

        friends_of_friends = self.network.get_friends_of_friends(self.user1)
        self.assertEqual(friends_of_friends, [self.user3])

    def test_friend_count_property(self):
        self.network.add_user(self.user1)
        self.network.add_user(self.user2)

        self.user1.add_friend(self.user2)

        self.assertEqual(self.user1.friend_count, 1)
        self.assertEqual(self.user2.friend_count, 1)

    def test_mutual_friend_count_property(self):
        self.network.add_user(self.user1)
        self.network.add_user(self.user2)
        self.network.add_user(self.user3)

        self.user1.add_friend(self.user2)
        self.user1.add_friend(self.user3)
        self.user2.add_friend(self.user3)

        self.assertEqual(self.user1.mutual_friend_count(self.user2), 1)
        self.assertEqual(self.user1.mutual_friend_count(self.user3), 1)

if __name__ == '__main__':
    unittest.main()