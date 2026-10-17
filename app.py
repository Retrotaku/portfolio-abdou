from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from flask import Flask, abort, render_template

from portfolio_data import PORTFOLIO


BASE_DIR = Path(__file__).resolve().parent
CV_PATH = BASE_DIR / "static" / "files" / "cv-abdou-salifou.pdf"


def create_app(test_config: dict[str, Any] | None = None) -> Flask:
    app = Flask(__name__)
    if test_config:
        app.config.update(test_config)

    @app.context_processor
    def inject_portfolio() -> dict[str, Any]:
        return {"portfolio": PORTFOLIO, "cv_available": CV_PATH.is_file()}

    @app.get("/")
    def index() -> str:
        return render_template("index.html")

    @app.get("/projets/<slug>")
    def project_detail(slug: str) -> str:
        project = next(
            (item for item in PORTFOLIO["projects"] if item["slug"] == slug),
            None,
        )
        if project is None:
            abort(404)
        return render_template("project.html", project=project)

    @app.errorhandler(404)
    def page_not_found(error: Exception) -> tuple[str, int]:
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_server_error(error: Exception) -> tuple[str, int]:
        return render_template("500.html"), 500

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=int(os.environ.get("PORT", "5000")),
        debug=False,
    )
