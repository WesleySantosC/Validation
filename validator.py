from pathlib import Path
from dotenv import dotenv_values
import sys
import yaml

BASE_DIR = Path(__file__).resolve().parent
VARIABLES_FILE = BASE_DIR / "variables.yaml"

if len(sys.argv) != 2:
    print(f"Uso: python3 {Path(sys.argv[0]).name} <arquivo.env>")
    sys.exit(1)

env_file = Path(sys.argv[1])

if not env_file.is_file():
    print(f"❌ Arquivo não encontrado: {env_file}")
    sys.exit(1)

with VARIABLES_FILE.open() as file:
    config = yaml.safe_load(file)

env = dotenv_values(env_file)

valid = True

print(f"OpenTelemetry Standard v{config['version']}\n")

for name, settings in config["variables"].items():
    value = env.get(name)

    if settings.get("required") and not value:
        print(f"❌ {name} não definida")
        valid = False
    else:
        print(f"✅ {name} configurada")

if valid:
    print("\n✅ Configuração válida.")
else:
    print("\n❌ Configuração inválida.")
    sys.exit(1)