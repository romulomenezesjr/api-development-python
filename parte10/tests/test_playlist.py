from app.schemas import Playlist
from fastapi import status

def test_create_playlists(authorized_client):
    res = authorized_client.post("/playlists/", json={
        "title": "Test ",
        "thumbnail": "",
        "description": "test playlist",
        "published": "True"
    })
    p = Playlist(**res.json())
    assert p.id == 1
    assert res.status_code == status.HTTP_201_CREATED

def test_get_all_playlists(test_playlists, authorized_client):
    res = authorized_client.get("/playlists/")

    playlists = map( lambda p: Playlist(**p.get("PlaylistModel")), res.json() )

    for p in playlists:
        assert p.title.find("Test") >= 0 

    assert res.status_code == status.HTTP_200_OK
