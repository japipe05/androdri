# dash_test/coverage_dashboard_plotly.py
import json
from pathlib import Path
import dash
from dash import dcc, html
import plotly.graph_objects as go

# Ruta del JSON de coverage
coverage_json_path = Path("reports/coverage.json")
if not coverage_json_path.exists():
    raise FileNotFoundError(f"No se encontró el archivo {coverage_json_path}. Genera primero coverage JSON.")

with open(coverage_json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Preparar datos para el gráfico
files = data.get("files", {})
filenames = []
coverage_percent = []

for filename, info in files.items():
    summary = info.get("summary", {})
    filenames.append(filename)
    # coverage_percent usa el valor numérico
    coverage_percent.append(float(summary.get("percent_covered_display", "0").strip('%')))

# Crear aplicación Dash
app = dash.Dash(__name__, title="Coverage Dashboard")

app.layout = html.Div(style={"fontFamily": "Arial", "margin": "40px"}, children=[
    html.H1("Coverage Dashboard", style={"textAlign": "center", "color": "#2C3E50"}),
    html.P(f"Total archivos: {len(filenames)}", style={"textAlign": "center"}),
    dcc.Graph(
        figure=go.Figure(
            data=[go.Bar(
                x=filenames,
                y=coverage_percent,
                text=[f"{v}%" for v in coverage_percent],
                textposition="auto",
                marker_color=coverage_percent,
                marker_colorscale="Viridis",
            )],
            layout=go.Layout(
                title="Cobertura por archivo",
                xaxis_title="Archivo",
                yaxis_title="Cobertura (%)",
                yaxis=dict(range=[0, 100]),
                template="plotly_dark",
            )
        )
    ),
    html.P("Reporte HTML por defecto de coverage.py disponible en: reports/htmlcov/index.html",
           style={"textAlign": "center", "marginTop": "20px", "color": "#34495E"})
])

if __name__ == "__main__":
    # Dash 3+ usa app.run()
    app.run(debug=True)
