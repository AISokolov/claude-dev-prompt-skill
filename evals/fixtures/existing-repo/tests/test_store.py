from notes import store


def test_load_missing_file(tmp_path):
    assert store.load(tmp_path / "none.json") == []


def test_save_and_load_roundtrip(tmp_path):
    p = tmp_path / "n.json"
    store.save(p, [{"text": "a"}])
    assert store.load(p) == [{"text": "a"}]
