from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class UserModel (Model):
    
    class Meta:
        table_name = "user"
        host = "http://localhost:8003"
        email = UnicodeAttribute(null=True)1
        first_name = UnicodeAttribute(null=True)
        last_name = UnicodeAttribute(null=True)
        
if not UserModel.exists():
    UserModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True);