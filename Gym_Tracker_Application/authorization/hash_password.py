# from werkzeug.security import generate_password_hash

# def hash_password(request_data: dict) -> dict:
#     if request_data.get('password'):
#         hashed_password = generate_password_hash(request_data.get('password'))
#         request_data['password'] = hashed_password
#         return request_data
#     else:
#         return '500'