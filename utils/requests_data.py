
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

    add_daybook_body = {
        "client_id": 1,
        "task_type": "SINGLE TASK",
        "category_id": 1,
        "subcategory_id": 1,
        "fees": "5000",
        "advance": "7777",
        "balance": "88",
        "remark": "gkhsgkfgdkj",
        "employee_id": 1,
        "start_date": "2023-04-12",
        "end_date": "2023-04-12",
        "priority": "High"
    }

    add_bank_body = {
        "account_holder_name": "account_holder_ame name",
        "bank_name": "bank_name TASK",
        "branch_address": "branch_address",
        "account_number": "account_number",
        "ifsc_code": "ifsc_codefff",
        "micr_code": "micr_codeeeee"
    }

    add_partner_body = {
        "partner_name": "partner_name name",
        "pan": "pan TASK",
        "mobile": "mobile",
        "dob": "2023-05-09",
        "address": "address",
        "micr_code": "micr_codeeeee",
        "city": "city",
        "state": "state",
        "pin": "pin",
        "remark": "remarkaddress"
    }
