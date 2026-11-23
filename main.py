def test_login(user, password):
    if user == "admin" and password == "1234":
        print("SUCCES")
    else:
        print("FAIL")

test_login("admin", "1234")
test_login("user", "0000")
print("usuario 1")