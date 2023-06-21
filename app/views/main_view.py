from flask import render_template, Blueprint, url_for

bp = Blueprint("main", __name__, url_prefix="/")

@bp.route("/")
def index():
    return render_template("grandchild.html")