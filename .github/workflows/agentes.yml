name: Execucao de Multi-Agentes na Nuvem

on:
  workflow_dispatch:
    inputs:
      comando_usuario:
        description: 'O que voce quer que o grupo de agentes faca?'
        required: true
        default: 'Busque um repositorio e analise o codigo'

jobs:
  run-agents:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout do Repositorio
        uses: actions/checkout@v4

      - name: Configurar Ambiente Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Instalar Dependencias
        run: |
          pip install requests

      - name: Executar Grupo de Agentes
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python scripts/orquestrador_agentes.py "${{ github.event.inputs.comando_usuario }}"
