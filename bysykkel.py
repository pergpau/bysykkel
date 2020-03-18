
import requests
from collections import OrderedDict
import sys

class Bysykkelviser():

    def __init__(self):
        self.sources = self.update_sources()
        self.id_stations = self.build_id_stations()
        self.all_data = {}
       
    def update_sources(self):
        sources_url = 'https://gbfs.urbansharing.com/oslobysykkel.no/gbfs.json'

        return self.get_api_data(sources_url)

    def get_api_url(self, apiname):
        api_url = None
        for api in self.sources["data"]["nb"]["feeds"]:
            if api["name"] == apiname:
                api_url = api["url"]

        return api_url

    def get_api_data(self, url):
        header = {'Client-Identifier':'origosoknad-kodeoppgave'}
        api_data = {}
        try:
            raw_response = requests.get(url, headers=header)
            api_data = raw_response.json()
        except:
            print("\nKunne ikke hente data fra Bysykkel-API på URL:",url) 
            print("Avslutter programmet...\n")
            sys.exit()

        return api_data

    def build_id_stations(self):
        url = self.get_api_url("station_information")
        response = self.get_api_data(url)
        id_station_dict = {}
        for station in response["data"]["stations"]:
            station_id = station["station_id"]
            id_station_dict[station_id] = station["name"]

        return id_station_dict
    
    def build_view_data(self):
        status_url = self.get_api_url("station_status")
        current_status = self.get_api_data(status_url)
        
        for station in current_status["data"]["stations"]:
            if station["is_renting"] == 1:     
                idno = station["station_id"]
                name = self.id_stations[idno]
                docks = station["num_docks_available"]
                bikes = station["num_bikes_available"]
                self.all_data[idno] = {"name": name, "docks": docks, "bikes": bikes}
        self.all_data = OrderedDict(sorted(self.all_data.items(), key = lambda x: x[1]["name"]))

    def get_search_results(self,query):
        results = []     
        for idno, data in self.all_data.items():
            if query.lower() in data["name"].lower():
                results.append((data["name"], data["docks"], data["bikes"]))
        return results
        
    def show_availability(self, query=""):
        self.build_view_data()
        results = self.get_search_results(query)
        if len(results) > 0:
            print("\n{:<30}{:<15}{:<15}".format("STATIVNAVN","RETURPLASSER","LEDIGE SYKLER"))
            for result in results:
                print("{:<30}{:<15}{:<15}".format(result[0],result[1],result[2]))
        else:
            print("\nIngen stativer med navn '" + query + "' funnet.")    
        
        
    # def show_availability(self, query=""):
    #     query = query.lower()
    #     self.build_view_data()
    #     print(query)
    #     if any(query in station["name"].lower() for station in self.all_data.values()):
    #         print("\n{:<30}{:<15}{:<15}".format("STATIVNAVN","RETURPLASSER","LEDIGE SYKLER"))
    #         for idno, data in self.all_data.items():
    #             if query in data["name"].lower():
    #                 print("{:<30}{:<15}{:<15}".format(data["name"], data["docks"], data["bikes"]))
    #     else:
    #         print("\nIngen stativer med navn '" + query + "' funnet.")    
        

    def run(self):
        print("\nOSLO BYSYKKEL - Finn stativer med ledige sykler og returplasser")
        inp = ""
        while inp != "0":
            print("\nDine valg:")
            print("1. Søk etter sykkelstativ")
            print("2. Vis status for alle sykkelstativer")
            print("0. Avslutt")
            inp = input("\nDitt valg: ")
            if inp == "1":
                query = input("Skriv stativnavn: ")
                self.show_availability(query)
            elif inp == "2":
                self.show_availability()
            else:
                print("\nVelg 1, 2 eller 0 for å avslutte")

        print("\nAvslutter... Velkommen igjen!\n")

if __name__ == "__main__":
    app = Bysykkelviser()
    app.run()
