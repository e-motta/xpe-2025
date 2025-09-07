from flask import Blueprint, request, make_response, Response, jsonify


api_route_blueprint = Blueprint("api", __name__, url_prefix="/api/v1")


@api_route_blueprint.route("/", methods=["POST"])
def conversation_post() -> Response:
    if request.json is None:
        return make_response("No data", 400)

    try:
        pass
        # TODO: process messages
    except Exception as e:
        return make_response(str(e), 500)

    return make_response("OK", 200)
