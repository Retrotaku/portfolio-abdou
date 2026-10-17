from __future__ import annotations

from html import escape

from app import create_app
from portfolio_data import PORTFOLIO


def make_client():
    app = create_app({"TESTING": True})
    return app, app.test_client()


def test_homepage_renders_required_sections_and_contact_details():
    _, client = make_client()
    response = client.get("/")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    for section_id in (
        'id="accueil"',
        'id="a-propos"',
        'id="competences"',
        'id="projets"',
        'id="formation"',
        'id="contact"',
    ):
        assert section_id in page
    for detail in (
        "Abdou Salifou",
        "Abidjan, Côte d&#39;Ivoire",
        "bachirabdou2468@gmail.com",
        "0104704192",
        "4 à 6 mois",
    ):
        assert detail in page
    assert f'href="mailto:{PORTFOLIO["email"]}"' in page
    assert f'href="tel:{PORTFOLIO["phone"]}"' in page
    assert f'href="{escape(PORTFOLIO["linkedin"], quote=True)}"' in page
    assert f'href="{PORTFOLIO["github"]}"' in page
    assert "Télécharger mon CV" not in page
    assert "CV bientôt disponible" in page


def test_project_details_render_and_unknown_project_is_404():
    _, client = make_client()

    response = client.get("/projets/gestion-scolaire-emsp")
    assert response.status_code == 200
    assert "Technologies envisagées — à confirmer" in response.get_data(as_text=True)

    missing = client.get("/projets/inconnu")
    assert missing.status_code == 404
    assert "Cette page n'existe pas." in missing.get_data(as_text=True)


def test_static_assets_are_served():
    _, client = make_client()

    css = client.get("/static/css/style.css")
    script = client.get("/static/js/main.js")
    favicon = client.get("/static/images/favicon.svg")

    assert css.status_code == 200
    assert "prefers-reduced-motion" in css.get_data(as_text=True)
    assert script.status_code == 200
    assert "aria-expanded" in script.get_data(as_text=True)
    assert favicon.status_code == 200


def test_custom_server_error_page_is_returned():
    app, client = make_client()
    app.config["PROPAGATE_EXCEPTIONS"] = False

    def fail_for_test():
        raise RuntimeError("test-only failure")

    app.add_url_rule("/__test_error__", view_func=fail_for_test)
    response = client.get("/__test_error__")

    assert response.status_code == 500
    assert "Une erreur est survenue." in response.get_data(as_text=True)


def test_cv_link_appears_only_when_file_exists(tmp_path, monkeypatch):
    import app as app_module

    cv_file = tmp_path / "cv-abdou-salifou.pdf"
    monkeypatch.setattr(app_module, "CV_PATH", cv_file)
    app = app_module.create_app({"TESTING": True})

    assert "CV bientôt disponible" in app.test_client().get("/").get_data(as_text=True)

    cv_file.write_bytes(b"%PDF-1.4 test")
    page = app.test_client().get("/").get_data(as_text=True)
    assert "Télécharger mon CV" in page
    assert "/static/files/cv-abdou-salifou.pdf" in page
