
class request_data:

    register_new_user_body = {
        "name": "testuser",
        "email": "ayush.developerbox+14@gmail.com",
        "password": "12345678",
        "password_confirmation": "12345678"
    }

    login_body = {
        "email": "ayush.developerbox+2@gmail.com",
        "password": "12345678"
    }

    add_client_body = {
        "type": "Lead/Query 3",
        "name": "test CFSM 3",
        "phone": "9876543210",
        "module": "GST"
    }

    update_client_body = {
        "type": "updated Lead/Query",
        "name": "updated test client",
        "phone": "989786767",
        "module": "New - GST"
    }

    add_category_body = {
        "name": "new Category ",
        "description": "desc"
    }