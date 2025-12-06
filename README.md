# Mini Turtle 🐢

Un paquete sencillo que permite dibujar con texto usando movimientos básicos:

- `adelante(pasos)`
- `abajo(pasos)`
- `reiniciar()`

Este paquete mantiene un estado interno (`posición_x`) para simular dibujos tipo tortuga.

---

## 🚀 Instalación (local)

Para instalar este paquete localmente, desde la carpeta del proyecto:

```bash
pip install .

from mini_turtle import adelante, abajo, reiniciar

print("Dibujo de prueba:\n")

adelante(3)   # ---
abajo(2)      # |
              # |

reiniciar()

mini_turtle_task/
├── mini_turtle/
│   ├── __init__.py
│   └── drawer_logic.py
├── main.py
├── README.md
└── pyproject.toml


print("\nDespués de reiniciar:\n")
adelante(4)   # ----

