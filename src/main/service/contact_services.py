import uuid
import re
import datetime as dt

from main import db
from main.model.user import Users, Contact

def save_contacts(data_contacts, user):
    Contacts = []
    if user and user.id:
        for contact in data_contacts:
            contact['user_id'] = user.id
            Contacts.append(Contact(contact))

    try:
        db.session.add_all(Contacts)
        db.session.commit()
        return {'message' : 'success'}
    except:
        return {'message' : 'fail'}

def edit_user(data, id):
    user = Contact.query.filter_by(id = id).first()
    if user:
        user.updatePropertiesC(data)

        try:
            db.session.commit()
            response_object = {
                'status': 'Success',
                'message': 'Contact updated successfully.'
            }
            return response_object, 201
        except:
            response_object = {
                'status': 'Fail',
                'message': 'The user does not exist'
            }
            return response_object, 400
            


def delete_one_contact(user_id):
    user = Contact.query.filter_by(id = id).first()
    if user:
        delete_delete(user)
        response_object = {
            'status': 'success',
            'message': 'Successfully eliminated.'
        }
        return response_object, 201



def get_contact(id):
    return Contact.query.filter_by(id = id).first()


def get_contacts(user_id):
    return Contact.query.filter_by(user_id=user_id).all()



def save_changes(data):
    db.session.add(data)
    db.session.commit()

def delete_contact(user):
    db.session.delete(user)
    db.session.commit()


   