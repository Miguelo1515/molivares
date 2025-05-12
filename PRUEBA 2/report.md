# Metodología

1. **Origen de datos**: se utilizaron archivos CSV meteorológicos para tres localidades (Salvador, Calama y Vallenar). Se realizó una limpieza de formato y valores extremos.
2. **Filtrado inteligente**: se aplicó un filtro híbrido que combina un método robusto por mes/hora para irradiancia y mediana deslizante para variables meteorológicas.
3. **Simulación PVWatts**: se configuró un sistema fotovoltaico de 50 MW_DC, relación DC/AC de 1.2, eficiencia del inversor 96 %, y pérdidas del sistema de 14 %, utilizando PySAM con PVWatts v8.
4. **Análisis económico**: se calcularon LCOE y VAN asumiendo una vida útil de 20 años y una tasa de FCR del 8 %.
5. **Sensibilidad**: se analizó la sensibilidad del LCOE frente a variables como CapEx, FCR, precio spot, pérdidas y vida útil.

# Conclusiones

- **Generación anual**: cada sitio mostró un comportamiento distinto en términos de producción horaria y total anual.
- **Eficiencia económica**: el LCOE varió principalmente con el CapEx y el FCR. Vallenar obtuvo el menor LCOE en condiciones base.
- **Variables críticas**: los gráficos tornado mostraron que CapEx y FCR son las variables más influyentes en el LCOE.
- **Recomendaciones**: enfocar esfuerzos en optimizar costos de inversión y estrategias de financiamiento para mejorar la rentabilidad.
