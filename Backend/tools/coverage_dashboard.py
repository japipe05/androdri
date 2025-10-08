import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from datetime import datetime

# === CONFIG ===
REPORT_JSON = Path("reports/coverage.json")
OUTPUT_HTML = Path("reports/coverage_dashboard.html")
HISTORY_FILE = Path("reports/coverage_history.json")

# === CARGAR REPORTE JSON ===
if not REPORT_JSON.exists():
    raise FileNotFoundError(f"No se encontró {REPORT_JSON}. Ejecuta primero:\n"
                            "coverage run -m pytest && coverage json -o reports/coverage.json")

with open(REPORT_JSON, "r", encoding="utf-8") as f:
    data = json.load(f)

# === PROCESAR DATOS ACTUALES ===
files = []
totals = data.get("totals", {})
current_total = totals.get("percent_covered", 0)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for filename, metrics in data.get("files", {}).items():
    files.append({
        "Archivo": filename,
        "Declaraciones": metrics["summary"]["num_statements"],
        "Faltantes": metrics["summary"]["missing_lines"],
        "Cobertura (%)": metrics["summary"]["percent_covered"],
    })

df = pd.DataFrame(files).sort_values(by="Cobertura (%)", ascending=False)

# === HISTÓRICO DE COBERTURA ===
HISTORY_FILE.parent.mkdir(exist_ok=True)

if HISTORY_FILE.exists():
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        history_data = json.load(f)
else:
    history_data = []

# Agregar registro actual al histórico
history_data.append({
    "fecha": timestamp,
    "cobertura_total": current_total
})

# Limitar a los últimos 30 registros
history_data = history_data[-30:]

# Guardar histórico actualizado
with open(HISTORY_FILE, "w", encoding="utf-8") as f:
    json.dump(history_data, f, indent=4, ensure_ascii=False)

# Crear DataFrame histórico
df_history = pd.DataFrame(history_data)

# === FIGURA 1: Cobertura por archivo ===
fig_files = px.bar(
    df,
    x="Archivo",
    y="Cobertura (%)",
    color="Cobertura (%)",
    color_continuous_scale="Bluered_r",
    text_auto=".1f",
    title="📊 Cobertura de Código por Archivo"
)
fig_files.update_layout(
    title_font_size=22,
    title_x=0.5,
    template="plotly_dark",
    xaxis_tickangle=-45,
    height=600,
    margin=dict(l=40, r=40, t=80, b=150)
)

# === FIGURA 2: Resumen general ===
fig_summary = go.Figure()
fig_summary.add_trace(go.Indicator(
    mode="gauge+number+delta",
    value=current_total,
    title={"text": "Cobertura total (%)"},
    gauge={
        "axis": {"range": [0, 100]},
        "bar": {"color": "green"},
        "steps": [
            {"range": [0, 60], "color": "#FF4C4C"},
            {"range": [60, 90], "color": "#FFD700"},
            {"range": [90, 100], "color": "#00CC96"},
        ],
    },
    domain={"x": [0, 1], "y": [0, 1]},
))
fig_summary.update_layout(
    title=f"Resumen General ({timestamp})",
    height=400,
    template="plotly_dark",
)

# === FIGURA 3: Histórico de cobertura ===
fig_history = px.line(
    df_history,
    x="fecha",
    y="cobertura_total",
    title="📈 Evolución Histórica de la Cobertura",
    markers=True
)
fig_history.update_traces(line_color="#00CC96", marker=dict(size=10, color="#FFD700"))
fig_history.update_layout(
    template="plotly_dark",
    title_font_size=22,
    title_x=0.5,
    height=400,
)

# === GENERAR HTML FINAL ===
output_html = f"""
<html>
<head>
    <title>📈 Reporte de Cobertura - FastAPI</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body style="background-color:#111;color:white;font-family:sans-serif;margin:0;padding:0;">
    <h1 style="text-align:center;padding:20px;">Reporte de Cobertura - Proyecto FastAPI</h1>
    <div style="text-align:center;font-size:14px;">Generado el: {timestamp}</div>
    <hr style="border:1px solid #444;">
    <div>{fig_summary.to_html(full_html=False, include_plotlyjs='cdn')}</div>
    <div>{fig_files.to_html(full_html=False, include_plotlyjs=False)}</div>
    <div>{fig_history.to_html(full_html=False, include_plotlyjs=False)}</div>
    <footer style="text-align:center;padding:15px;color:#777;font-size:13px;">
        Coverage Dashboard • {datetime.now().year}
    </footer>
</body>
</html>
"""

OUTPUT_HTML.write_text(output_html, encoding="utf-8")
print(f"✅ Dashboard generado en: {OUTPUT_HTML.resolve()}")
print(f"📈 Histórico guardado en: {HISTORY_FILE.resolve()}")
