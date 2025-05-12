Proyecto PV Simulation Dashboard

Requisitos

- Python ≥ 3.8
- pandas
- numpy
- matplotlib
- ipywidgets
- PySAM
- plotly (opcional, para visualización avanzada)

Instalación

pip install pandas numpy matplotlib ipywidgets PySAM plotly

Estructura de Archivos

PRUEBA_2/
├─ salvador_corrupted_filtrado.csv
├─ calama_corrupted_filtrado.csv
├─ vallenar_corrupted_filtrado.csv
├─ Salvador_ac_power.csv
├─ Calama_ac_power.csv
├─ Vallenar_ac_power.csv
├─ resumen_energia_total.csv
├─ resumen_economico.csv
├─ sensibilidad_economica.csv
├─ Dashboard.ipynb
├─ report.md
└─ README.md

Cómo ejecutar

1. Activar entorno virtual (si corresponde):
   source ~/SAM_prueba/bin/activate

2. Ejecutar Jupyter Notebook:
   jupyter notebook Dashboard.ipynb

3. Explorar el dashboard con los selectores interactivos.

Salidas

- *_ac_power.csv: potencia AC horaria para cada sitio.
- resumen_energia_total.csv: energía anual por sitio.
- resumen_economico.csv: LCOE y VAN por sitio.
- sensibilidad_economica.csv: sensibilidad del LCOE frente a variables clave.
- report.md: resumen metodológico y conclusiones.
