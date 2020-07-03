from app import db


class Task(db.Document):
    description = db.StringField(required=True)
    done = db.BooleanField(required=True)

    @classmethod
    def from_dict(cls, data):
        return Task(description=data['description'], done=data['done'])

    def to_dict(self):
        return {
            'id': str(self.id),
            'description': self.description,
            'done': self.done
        }
