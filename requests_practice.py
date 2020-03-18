import requests

# GET


def authors_list():
    base = requests.get("https://fakerestapi.azurewebsites.net/api/Authors")
    if base.status_code == 200:
        print('Authors list')
        authors = []
        for i in base.json():
            authors.append(str(i['FirstName']) + ' ' + str(i['LastName']))
        print(authors)
    else:
        return base.status_code


def author_by_id():
    base = requests.get("https://fakerestapi.azurewebsites.net/api/Authors")
    if base.status_code == 200:
        print('Author by id (id 5)')
        for i in base.json():
            if i['ID'] == 5:
                print(str(i['FirstName']) + ' ' + str(i['LastName']))
    else:
        return base.status_code

# POST


def add_book():
    new_book = requests.post("https://fakerestapi.azurewebsites.net/api/Books",
                                      json={
                                 "ID": 1991,
                                 "Title": "Sergey",
                                 "Description": "Test desc",
                                 "PageCount": 100,
                                 "Excerpt": "Excerpt",
                                 "PublishDate": "2020-02-26T16:42:32.419Z"
                             })
    print('Adding book status code: ' + str(new_book.status_code))


def add_user():
    new_user = requests.post("https://fakerestapi.azurewebsites.net/"
                             "api/Users",
                                      json={
                                 "ID": 1991,
                                 "UserName": "Sergey",
                                 "Password": "Test"
                             })
    print('Adding user status code: ' + str(new_user.status_code))


# PUT


def change_book():
    put_book = requests.put('https://fakerestapi.azurewebsites.net/'
                            'api/Books/1',
                                     json={
                                "ID": 1991,
                                "Title": "Sergey",
                                "Description": "Test desc",
                                "PageCount": 100,
                                "Excerpt": "Test",
                                "PublishDate": "2020-02-26T16:42:32.419Z"
                            })
    print('Updating book status code: ' + str(put_book.status_code))


# DELETE


def deleting_user():
    user_delete = requests.delete('https://fakerestapi.azurewebsites.net/'
                                  'api/Users/1')
    print('User deleting status code: ' + str(user_delete.status_code))


authors_list()
author_by_id()
add_book()
add_user()
change_book()
deleting_user()
