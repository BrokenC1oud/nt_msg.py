import nt_msg
import db


def main():
    print(len(db.session.query(db.GroupMessage).all()))


if __name__ == "__main__":
    main()
