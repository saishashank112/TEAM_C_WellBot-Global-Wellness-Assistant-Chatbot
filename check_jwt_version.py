import jwt
import sys

print(f"PyJWT Version: {jwt.__version__}")
secret = "test_secret"
token = jwt.encode({'sub': "1"}, secret, algorithm='HS256')

if isinstance(token, bytes):
    token = token.decode('utf-8')

print(f"Encoded: {token}")

try:
    decoded = jwt.decode(token, secret, algorithms=['HS256'])
    print(f"Decoded Success: {decoded}")
except Exception as e:
    print(f"Decoded FAILED: {e}")
