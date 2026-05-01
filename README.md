# AURA DRAIN
### AI-Based Smart Water Pollution Detection — Bellandur Lake

AI platform using Sentinel-2 satellite imagery, machine learning, and GIS to detect
water pollution zones and map drain networks around Bellandur Lake, Bengaluru.

## Quickstart
```bash
pip install -r requirements.txt
python src/ai/train_model.py
python src/gis/gis_processor.py
open src/dashboard/index.html
```

## Dashboard Login
| Role | Username | Password |
|------|----------|----------|
| BBMP Officer | bbmp_admin | bbmp2024 |
| Field Employee | field_user | field123 |

## Tech Stack
- AI: scikit-learn RandomForest on Sentinel-2 bands
- GIS: rasterio, geopandas, Leaflet.js
- Dashboard: HTML5, Chart.js, OpenStreetMap
