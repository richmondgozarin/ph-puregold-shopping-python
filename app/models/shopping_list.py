from app import db

class ShoppingList(db.Model):
    """This class represents the shoppinglist table."""

    __tablename__ = 'shoppinglists'

    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    item_id = db.Column(db.Integer, db.ForeignKey('item.id'),
        nullable=False)
    items = db.relationship('Item', backref=db.backref('shoppinglists', lazy=True))

    def __init__(self, name):
        """initialize with name."""
        self.store_name = name

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self, name):
        self.store_name = name
        db.session.commit()

    @staticmethod
    def get_all():
        return ShoppingList.query.all()
    
    @staticmethod
    def get_by_store_name(store_name):
        return ShoppingList.query.filter_by(store_name=store_name).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<ShoppingList: {}>".format(self.name)