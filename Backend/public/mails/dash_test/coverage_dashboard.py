"""
===============================================================================
Archivo:        coverage_dashboard_plotly.py
Ubicación:      dash_test/coverage_dashboard_plotly.py
Descripción:    Dashboard interactivo de cobertura ejecutado en un servidor Dash.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/11/10
Radicado:       v0008af
===============================================================================
"""

import json
import pandas as pd
from pathlib import Path
from datetime import datetime
from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go

# === CONFIG ===
REPORT_JSON = Path("reports/coverage.json")
HISTORY_FILE = Path("reports/coverage_history.json")

# === CARGAR REPORTE JSON ===
if not REPORT_JSON.exists():
    raise FileNotFoundError(
        f"No se encontró {REPORT_JSON}. Ejecuta primero:\n"
        "coverage run -m pytest && coverage json -o reports/coverage.json"
    )

with open(REPORT_JSON, "r", encoding="utf-8") as f:
    data = json.load(f)

# === PROCESAR DATOS ===
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

# === HISTÓRICO ===
HISTORY_FILE.parent.mkdir(exist_ok=True)
if HISTORY_FILE.exists():
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        history_data = json.load(f)
else:
    history_data = []

history_data.append({"fecha": timestamp, "cobertura_total": current_total})
history_data = history_data[-30:]
with open(HISTORY_FILE, "w", encoding="utf-8") as f:
    json.dump(history_data, f, indent=4, ensure_ascii=False)

df_history = pd.DataFrame(history_data)

# === GRÁFICOS ===
fig_files = px.bar(
    df, x="Archivo", y="Cobertura (%)",
    color="Cobertura (%)", color_continuous_scale="Bluered_r",
    text_auto=".1f", title="📊 Cobertura por Archivo"
)
fig_summary = go.Figure(go.Indicator(
    mode="gauge+number",
    value=current_total,
    title={"text": "Cobertura Total (%)"},
    gauge={
        "axis": {"range": [0, 100]},
        "bar": {"color": "#00CC96"},
        "steps": [
            {"range": [0, 60], "color": "#FF4C4C"},
            {"range": [60, 90], "color": "#FFD700"},
            {"range": [90, 100], "color": "#00CC96"},
        ],
    },
))
fig_history = px.line(
    df_history, x="fecha", y="cobertura_total",
    title="📈 Evolución Histórica de la Cobertura", markers=True
)
fig_history.update_traces(line_color="#00CC96", marker=dict(size=8, color="#FFD700"))

# === DASH APP ===
app = Dash(__name__)
app.title = "📈 Coverage Dashboard - FastAPI"

app.layout = html.Div(
    style={"backgroundColor": "#111", "color": "white", "fontFamily": "Arial"},
    children=[
        html.H1("Reporte de Cobertura - Proyecto FastAPI", style={"textAlign": "center"}),
        html.Div(f"Generado el: {timestamp}", style={"textAlign": "center", "marginBottom": 20}),
        dcc.Graph(figure=fig_summary),
        dcc.Graph(figure=fig_files),
        dcc.Graph(figure=fig_history),
        html.Footer(
            f"Coverage Dashboard • {datetime.now().year}",
            style={"textAlign": "center", "color": "#777", "padding": "15px"},
        ),
    ],
)

if __name__ == "__main__":
    print("🚀 Iniciando Coverage Dashboard en http://127.0.0.1:8050")
    app.run(host="127.0.0.1", port=8050, debug=False)

