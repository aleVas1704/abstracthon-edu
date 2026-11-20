from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_home_shows_three_practice_topics() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert 'aria-labelledby="practice-title"' in response.text
    assert "Funciones matemáticas" in response.text
    assert "Comprensión lectora" in response.text
    assert "Inglés básico" in response.text


def test_practice_link_opens_selected_preview_topic() -> None:
    home = client.get("/")

    assert "/preview?tema=Funciones%20matem%C3%A1ticas" in home.text
    preview = client.get("/preview", params={"tema": "Funciones matemáticas"})

    assert preview.status_code == 200
    assert "Funciones matemáticas" in preview.text
