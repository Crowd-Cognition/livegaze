from flask_sqlalchemy import SQLAlchemy
from flask_app.extensions.base_model import Base
from flask_redis import FlaskRedis
from flask_app.extensions.redis_constants import TRACKERS_SET, RECORD
from sqlalchemy import text

db = SQLAlchemy()

redis_client = FlaskRedis()


def init_db(app):
    db.init_app(app)
    redis_client.init_app(app)
    #remove the set from redis
    redis_client.delete(TRACKERS_SET)
    #stop last recording
    redis_client.set(RECORD, 'False')
    with app.app_context():
        db.session.execute(text("""
                    CREATE SEQUENCE IF NOT EXISTS board_tag_id_seq
                        AS bigint
                        START WITH 4
                        INCREMENT BY 1
                        MINVALUE 1
                        MAXVALUE 9223372036854775807
                        NO CYCLE
                        CACHE 1;
        """))
        db.session.commit()
        Base.metadata.create_all(db.engine)
        db.create_all()
        db.session.commit()




