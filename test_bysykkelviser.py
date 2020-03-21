from bysykkelviser import Bysykkelviser

def test_constructor():
    app = Bysykkelviser()
    assert type(app.sources) == dict
    assert len(app.sources) == 3
    assert type(app.id_stations) == dict
    assert len(app.id_stations) > 0

def test_api_url():
    app = Bysykkelviser()
    assert "last_updated" in app.sources
    url = app.get_api_url("station_information")
    assert url != None
    assert type(url) == str
    assert "station_information.json" in url

def test_api_data():
    app = Bysykkelviser()
    url = app.get_api_url("station_information")
    assert app.get_api_data(url) != None 
    assert type(app.get_api_data(url)) == dict

def test_id_station_build():
    app = Bysykkelviser()
    id_dict = app.build_id_stations()
    assert type(id_dict) == dict
    assert len(id_dict.keys()) > 0

def test_view_build():
    app = Bysykkelviser()
    app.build_view_data()
    assert type(app.all_data) == dict
    assert len(app.all_data.values()) > 0 

def test_search():
    app = Bysykkelviser()
    assert len(app.get_search_results("ABCDEFG")) == 0
    assert len(app.get_search_results("plass")) > 0
    
    all_results = app.get_search_results("")
    assert len(all_results) > 0
    assert all_results == sorted(all_results, key=lambda x:x["name"])


if __name__ == "__main__":
    test_constructor()
    test_api_url()
    test_api_data()
    test_id_station_build()
    test_view_build()
    test_search()
    