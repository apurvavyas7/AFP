from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = "admin123"
hashed = pwd_context.hash(password)

print("Original: ", password)
print("Hashed: ", hashed)

print("Valid", pwd_context.verify(password, hashed))