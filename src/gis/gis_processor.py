import json, os
from datetime import datetime

OUTPUT_DIR  = "../../outputs"
DRAIN_LOCATIONS = [
    {"id":"D-01","name":"Varthur Road Inlet","lat":12.9380,"lon":77.6740,"flow":42.3,"level":"high"},
    {"id":"D-02","name":"AECS Layout Nala","lat":12.9360,"lon":77.6810,"flow":18.7,"level":"medium"},
    {"id":"D-03","name":"HSR Sector 2 Drain","lat":12.9300,"lon":77.6850,"flow":31.5,"level":"high"},
    {"id":"D-04","name":"Iblur Junction","lat":12.9270,"lon":77.6900,"flow":9.2,"level":"low"},
    {"id":"D-05","name":"Doddakannalli Nala","lat":12.9410,"lon":77.6820,"flow":55.8,"level":"high"},
]
POLLUTION_ZONES = [
    {"zone_id":"Z-01","label":"High Pollution North","level":"high","index":82.4,"area_ha":14.2},
    {"zone_id":"Z-02","label":"Industrial Outlet","level":"high","index":78.1,"area_ha":9.8},
    {"zone_id":"Z-03","label":"Central Lake","level":"medium","index":55.6,"area_ha":28.5},
    {"zone_id":"Z-04","label":"East Shore","level":"low","index":22.3,"area_ha":11.7},
]

def run():
    print("=== AURA DRAIN — GIS Processing ===")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    drains = {"type":"FeatureCollection","features":[
        {"type":"Feature","geometry":{"type":"Point","coordinates":[d["lon"],d["lat"]]},
         "properties":d} for d in DRAIN_LOCATIONS]}
    with open(f"{OUTPUT_DIR}/drain_network.geojson","w") as f:
        json.dump(drains,f,indent=2)
    print(f"Exported {len(DRAIN_LOCATIONS)} drain points")
    print("\nHotspot zones by pollution index:")
    for z in sorted(POLLUTION_ZONES,key=lambda x:-x["index"]):
        print(f"  {z['zone_id']}  {z['label']:<28} index={z['index']}  area={z['area_ha']}ha")
    print("\nDone.")

if __name__ == "__main__":
    run()
