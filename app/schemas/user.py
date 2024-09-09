from digital_twin_migration.models.efficiency_app import User

from core.schema import ma

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
