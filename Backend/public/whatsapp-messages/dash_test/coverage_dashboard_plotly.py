# dash_test/coverage_dashboard_plotly.py
import json
from pathlib import Path
import dash
from dash import dcc, html
import plotly.graph_objects as go
import statistics

REPORTS_DIR = Path("reports")
COVERAGE_JSON = REPORTS_DIR / "coverage.json"
HTML_REPORT = REPORTS_DIR / "htmlcov" / "index.html"

if not COVERAGE_JSON.exists():
    raise FileNotFoundError(
        f"\n❌ No se encontró el archivo {COVERAGE_JSON}. "
        "Ejecuta antes: coverage run -m pytest && coverage json -o reports/coverage.json"
    )

with open(COVERAGE_JSON, "r", encoding="utf-8") as f:
    data = json.load(f)

files = data.get("files", {})
filenames, coverage_percent = [], []

for filename, info in files.items():
    summary = info.get("summary", {})
    percent_str = summary.get("percent_covered_display", "0").replace("%", "").strip()
    filenames.append(filename)
    coverage_percent.append(float(percent_str))

avg_coverage = round(statistics.mean(coverage_percent), 2) if coverage_percent else 0.0

# Figura con colores dinámicos
fig = go.Figure(
    data=[
        go.Bar(
            x=filenames,
            y=coverage_percent,
            text=[f"{v:.1f}%" for v in coverage_percent],
            textposition="auto",
            marker=dict(
                color=coverage_percent,
                colorscale="Viridis",
                colorbar=dict(title="Cobertura (%)"),
            ),
        )
    ]
)

fig.update_layout(
    title=f"Cobertura de Código por Archivo (Promedio: {avg_coverage}%)",
    xaxis_title="Archivo",
    yaxis_title="Cobertura (%)",
    yaxis=dict(range=[0, 100]),
    template="plotly_dark",
    hovermode="x unified",
    margin=dict(l=40, r=40, t=80, b=150),
)

app = dash.Dash(__name__, title="Coverage Dashboard")

app.layout = html.Div(
    style={"fontFamily": "Arial", "margin": "40px"},
    children=[
        html.H1("📊 Coverage Dashboard", style={"textAlign": "center", "color": "#16A085"}),
        html.H3(f"Archivos analizados: {len(filenames)}", style={"textAlign": "center", "color": "#BDC3C7"}),
        dcc.Graph(figure=fig),
        html.Div(
            [
                html.P("Ver reporte HTML completo:", style={"marginBottom": "4px"}),
                html.A(
                    "Abrir HTML Report",
                    href=str(HTML_REPORT),
                    target="_blank",
                    style={"color": "#3498DB", "fontWeight": "bold"},
                ),
            ],
            style={"textAlign": "center", "marginTop": "30px"},
        ),
    ],
)

if __name__ == "__main__":
    print("🚀 Iniciando Coverage Dashboard en http://127.0.0.1:8050")
    app.run(debug=False, use_reloader=False)
