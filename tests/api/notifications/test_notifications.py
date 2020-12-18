from api.notifications.notifications import Notifications


def test_create_destination():
    res = Notifications().create_destination()
    print(res)
