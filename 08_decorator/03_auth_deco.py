from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("❌ Access denied. Admins only.")
            return None
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_chai_inventory(user):
    print("🍵 Accessing chai inventory...")

access_chai_inventory("admin")