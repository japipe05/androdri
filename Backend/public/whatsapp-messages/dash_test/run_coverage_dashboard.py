import subprocess
from pathlib import Path

def run_command(cmd: str):
    print(f"▶ Ejecutando: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        raise RuntimeError(f"❌ Error al ejecutar: {cmd}")

def main():
    reports_path = Path("reports")
    reports_path.mkdir(exist_ok=True)

    print("🧪 Ejecutando pruebas y generando reportes de cobertura...")
    run_command("coverage run -m pytest")

    print("📊 Exportando cobertura a JSON...")
    run_command("coverage json -o reports/coverage.json")

    print("🧠 Mostrando cobertura en consola...")
    run_command("coverage report -m")

    print("🌐 Generando reporte HTML...")
    run_command("coverage html")

    print("🚀 Iniciando Dashboard interactivo...")
    run_command("python dash_test/coverage_dashboard_plotly.py")

if __name__ == "__main__":
    main()
