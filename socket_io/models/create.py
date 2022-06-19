import logging
import sqlalchemy

from __init__ import database
from constants import NEW_USER_ADDED, FAILED_TO_ADD_NEW_USER, USER_ALREADY_EXISTS
from models.entity import Users

logger = logging.getLogger(__name__)
def add_new_user(details):
    try:
        user = Users(**details)
        database.session.add(user)
        database.session.commit()
        response = NEW_USER_ADDED
    except (sqlalchemy.exc.IntegrityError, sqlalchemy.exc.PendingRollbackError):
        database.session.rollback()
        response = USER_ALREADY_EXISTS
    except Exception as why:
        response = FAILED_TO_ADD_NEW_USER
        logger.error("Failed to add a new user: %s", why)

    return response
