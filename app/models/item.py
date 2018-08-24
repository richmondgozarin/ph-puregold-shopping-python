from app import db

class Item(db.Model):
    """This class represents the item table."""

    __tablename__ = 'items'

    item_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    item_name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
    
    shopping_id = db.Column(db.Integer, db.ForeignKey('shoppinglists.shopping_id'),
        nullable=False)

    def __init__(self, name):
        """initialize with name."""
        self.item_name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Item.query.all()

    @staticmethod
    def get_item(shopping_id, item_name):
        return Item.query.filter_by(shopping_id=shopping_id, item_name=item_name).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<ShoppingItem: {}>".format(self.name)