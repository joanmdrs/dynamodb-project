from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class UserModel (Model):
    
    class Meta:
        table_name = "dynamodb-user"
        host = "http://localhost:8000"
        region = 'us-west-2'
    email = UnicodeAttribute(hash_key=True)
    first_name = UnicodeAttribute()
    last_name = UnicodeAttribute()
        
if not UserModel.exists():
    UserModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True);