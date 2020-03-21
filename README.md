# Oslo Bysykkel-app

## bysykkelviser.py
Enkelt terminal-basert Python-program som du kan bruke til å sjekke status (ledige ruterplasser og sykler) for bysykkelstativer i sanntid.

### Hvordan kjøre
Kan kjøres fra terminal med `python3 bysykkelviser.py`  
Krever ingen ekstra moduler utover vanlig Python3.6+-installasjon.

Tester for programmet kan kjøres med `python3 test_bysykkelviser.py` (eller ved å bruke pytest)

## bysykkel_api.py
REST-API for bysykkelviseren laget med Python-modulen Flask. Med APIet kan du hente sanntidsdata om status for sykkelstativene i JSON-format.

### Hvordan kjøre
Kan kjøres fra terminal med `python3 bysykkel_api.py`  
Se requirements.txt for dependencies. Kjøres som standard på http://localhost:5000/

### API-instruks
Følgende URI-er kan benyttes med GET-metoden:   
#### /api/stations
Henter alle bysykkelstativer (stations) i bruk med følgende data: stasjons-id, stasjonsnavn, ledige returplasser og ledige sykler.

```json
[
    {
        "bikes": 14,
        "docks": 6,
        "id": "623",
        "name": "7 Juni Plassen"
    },
    {
        "bikes": 2,
        "docks": 6,
        "id": "425",
        "name": "Adamstuen"
    },
...
    {
        "bikes": 0,
        "docks": 24,
        "id": "605",
        "name": "Økernveien"
    }
]
```

#### /api/stations?q=SØKEORD
Henter data om alle sykkelstativer som matcher søkeordet. F.eks. /api/stations?q=vippe

```json
[
    {
        "bikes": 7,
        "docks": 23,
        "id": "452",
        "name": "Vippetangen vest"
    },
    {
        "bikes": 1,
        "docks": 14,
        "id": "441",
        "name": "Vippetangen øst"
    }
]
```

#### /api/stations/STASJONS-ID
Henter data om et enkelt sykkelstativ etter id. F.eks. /api/stations/549

```json
{
    "bikes": 6,
    "docks": 15,
    "id": "549",
    "name": "Linaaes gate"
}
```

## Lisenser
Sanntidsdata er hentet fra https://oslobysykkel.no/apne-data/sanntid, gjort tilgjengelig under Norsk lisens for offentlige data (NLOD) 2.0