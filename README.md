# Web Traffic Analytics Report

## Overview  
This project performs detailed analytics on synthetic e-commerce session data, revealing web performance metrics and user behavior patterns using Python.

## Objective  
- Analyze key KPIs: bounce rate, conversion rate, session duration  
- Visualize traffic patterns, top pages, and device usage  
- Simulate funnel performance and time-based engagement metrics

## Dataset & Inputs  
- Source: `web_traffic.csv` (synthetic)  
- Key columns: `session_id`, `timestamp`, `page`, `device`, `source`, `duration`, `bounce`, `conversion`  
- Targets: Bounce and Conversion metrics

## Technologies Used  
Python, Pandas, Matplotlib, Seaborn

## How to Run  

### Script Mode  
```bash
python web_analytics_analysis.py
```

## Workflow  
- Load and preprocess web analytics dataset  
- Compute KPIs and breakdowns by category (source, device, page, hour)  
- Generate visualizations: bar charts, pie charts, heatmaps, histograms

## Results  
- Bounce rate, conversion rate, and session duration stats  
- Top pages and peak traffic hours  
- 9+ visualizations covering funnel drop-offs, heatmaps, page popularity

## Feature Importance (N/A)  
This project is exploratory/analytical, not predictive.

## Key Takeaways  
- Bounce rate and conversions vary significantly by source and device  
- Funnel insights reveal drop-offs between cart and thank-you stages  
- Time-based heatmaps help identify user engagement peaks

## Future Enhancements  
- Integrate session path analysis  
- Add cohort analysis by user ID  
- Export summary reports as PDF/CSV
