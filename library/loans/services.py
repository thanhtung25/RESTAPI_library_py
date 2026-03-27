from datetime import datetime
from flask import request, jsonify
from library.extension import db
from library.library_ma import LoansSchema
from library.model import Loans

loan_schema = LoansSchema()
loans_schema = LoansSchema(many=True)


def add_loan_service():
    data = request.get_json()
    required_fields = ["id_user", "id_copy", "issue_date", "return_date"]
    if not data:
        return jsonify({"error": "No data"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    try:
        issue_date = datetime.strptime(data["issue_date"], "%Y-%m-%d").date()
        return_date = datetime.strptime(data["return_date"], "%Y-%m-%d").date()
        actual_return_date = None
        if data.get("actual_return_date"):
            actual_return_date = datetime.strptime(data["actual_return_date"], "%Y-%m-%d").date()

        new_loan = Loans(
            id_user=data["id_user"],
            id_copy=data["id_copy"],
            issue_date=issue_date,
            return_date=return_date,
            actual_return_date=actual_return_date,
            status=data.get("status", "borrowed"),
            renewal_count=data.get("renewal_count", 0)
        )

        db.session.add(new_loan)
        db.session.commit()
        return jsonify(loan_schema.dump(new_loan)), 201
    except ValueError:
        db.session.rollback()
        return jsonify({"error": "Date format must be YYYY-MM-DD"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def get_all_loan_services():
    loans = Loans.query.all()
    return jsonify(loans_schema.dump(loans)), 200


def get_loan_by_id_services(id_loan):
    loan = Loans.query.get(id_loan)
    if not loan:
        return jsonify({"message": "Not found loan"}), 404
    return jsonify(loan_schema.dump(loan)), 200


def update_loan_by_id_services(id_loan):
    loan = Loans.query.get(id_loan)
    data = request.get_json()

    if not loan:
        return jsonify({"message": "Not found loan"}), 404
    if not data:
        return jsonify({"error": "No data"}), 400

    try:
        for field in ["id_user", "id_copy", "status", "renewal_count"]:
            if field in data:
                setattr(loan, field, data[field])

        if "issue_date" in data:
            loan.issue_date = datetime.strptime(data["issue_date"], "%Y-%m-%d").date()
        if "return_date" in data:
            loan.return_date = datetime.strptime(data["return_date"], "%Y-%m-%d").date()
        if "actual_return_date" in data:
            loan.actual_return_date = datetime.strptime(data["actual_return_date"], "%Y-%m-%d").date()

        db.session.commit()
        return jsonify(loan_schema.dump(loan)), 200
    except ValueError:
        db.session.rollback()
        return jsonify({"error": "Date format must be YYYY-MM-DD"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()


def delete_loan_by_id_services(id_loan):
    loan = Loans.query.get(id_loan)
    if not loan:
        return jsonify({"message": "Not found loan"}), 404

    try:
        db.session.delete(loan)
        db.session.commit()
        return jsonify({"message": "Loan deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()

def get_loan_by_user_id_service(id_user):
    loans = Loans.query.filter_by(id_user=id_user).all()
    schema = LoansSchema(many=True)

    return jsonify(schema.dump(loans)), 200
