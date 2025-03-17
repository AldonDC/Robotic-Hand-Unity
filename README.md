# 🖐️ Robotic Hand Unity - Python API Integration

<p align="center">
  <img src="https://github.com/user-attachments/assets/69170457-058a-40eb-96dd-02b21ee13c6b" width="50%">
</p>

## 📌 Overview
Este proyecto integra una mano robótica simulada en Unity con una API desarrollada en Python. Su objetivo principal es permitir la manipulación precisa de objetos mediante algoritmos avanzados de control y modelos matemáticos de agarre.

### 🌟 **Key Features**
✅ **Simulación de mano robótica en Unity**
✅ **API Python para control de movimiento en tiempo real**
✅ **Cinemática directa e inversa usando `roboticstoolbox`**
✅ **Comunicación fluida entre Python y Unity**
✅ **Manejo de errores y logging optimizado**
✅ **Actualizaciones en tiempo real con solicitudes API no bloqueantes**
✅ **Soporte para expansión de movimientos robóticos adicionales**

---


## 🔍 Introducción

El objetivo de este proyecto es desarrollar un algoritmo para manipular un objeto utilizando una pinza robótica simulada. Se utilizan técnicas matemáticas y físicas para modelar la interacción entre la mano robótica y el objeto, validando la solución mediante simulaciones y comparaciones con otras implementaciones.

## 📐 Fundamentos Matemáticos

### 📌 Ecuaciones del Robot  
Cada dedo de la mano robótica es modelado como una estructura de tres enlaces, similar a los dedos humanos. La punta del dedo se representa mediante una semiesfera que genera fuerzas de contacto para manipular el objeto.

**Ecuación del modelo del contacto:**  
<p align="center">
  <img src="https://latex.codecogs.com/png.latex?x^2%20+%20y^2%20+%20z^2%20=%20r^2,%20z%20\geq%200" />
</p>

Se considera una fuerza reactiva elástica en la punta del dedo, definida como:  
<p align="center">
  <img src="https://latex.codecogs.com/png.latex?F(x)%20=%20-kx" />
</p>

### 📌 Modelado del Contacto  
El objeto está en equilibrio cuando la suma de todas las fuerzas aplicadas sobre él es cero. Aplicando las leyes de Newton:  

<p align="center">
  <img src="https://latex.codecogs.com/png.latex?\sum%20F_o%20=%20F_{d1}%20-%20N_{d1}%20+%20F_{d2}%20-%20N_{d2}%20-%20F_{d3}%20+%20N_{d3}%20+%20g%20=%200" />
</p>

Se utilizan los principios de mecánica y cinemática para calcular las fuerzas de interacción entre los dedos y el objeto.

---

## 🔄 Cinemática

### 📌 Cinemática Directa
La posición final de la punta de cada dedo se obtiene mediante la multiplicación de matrices de transformación de Denavit-Hartenberg (DH):

<p align="center">
  <img src="https://latex.codecogs.com/png.latex?T^2_0%20=%20T^1_0%20\cdot%20T^2_1" />
</p>

**Expresiones de posición final:**
<p align="center">
  <img src="https://latex.codecogs.com/png.latex?x%20=%20\cos(q_1)%20+%20\cos(q_1%20+%20q_2)" />
</p>
<p align="center">
  <img src="https://latex.codecogs.com/png.latex?y%20=%20\sin(q_1)%20+%20\sin(q_1%20+%20q_2)" />
</p>
<p align="center">
  <img src="https://latex.codecogs.com/png.latex?\theta%20=%20q_1%20+%20q_2" />
</p>

### 📌 Cinemática Inversa
Para determinar los ángulos de los eslabones del dedo dados \(x\) e \(y\):

<p align="center">
  <img src="https://latex.codecogs.com/png.latex?q_2%20=%20\cos^{-1}%20\left(%20\frac{x^2%20+%20y^2%20-%202}{2}%20\right)" />
</p>

<p align="center">
  <img src="https://latex.codecogs.com/png.latex?q_1%20=%20\tan^{-1}%20\left(%20\frac{y}{x}%20\right)%20-%20q_2" />
</p>

Esto permite que la mano robótica alcance posiciones específicas al manipular el objeto.


## 🧪 Modelos de Agarre

El agarre de objetos con la mano robótica se modela considerando dos modos principales de contacto:

### 📌 Rodamiento y Deslizamiento  

Se definen dos modos principales de movimiento al sujetar el objeto:

1. **Rodamiento**: Cuando la velocidad relativa entre el objeto y la punta del dedo es cero en el punto de contacto.

   <p align="center">
      <img src="https://github.com/user-attachments/assets/482be951-9e81-441e-85d6-f02b503c119f" alt="Ecuación de Rodamiento">
   </p>

3. **Deslizamiento**: Ocurre cuando el punto de contacto cambia debido a la fricción:

   <p align="center">
      <img src="https://github.com/user-attachments/assets/21dd982e-d62d-4e49-b118-70a78c7d2345" alt="Ecuación de Deslizamiento">
   </p>


     

### 📌 Comparación de Modelos
| Característica | Rodamiento | Deslizamiento |
|--------------|------------|--------------|
| Tipo de contacto | Fijo | Variable |
| Fricción | Mantiene el objeto en contacto | Opuesta al movimiento |
| Modelado | Cinemática y dinámica | Fuerzas de fricción |

---

## ⚙️ Implementación

La implementación de la simulación se realizó en Python y Unity, utilizando herramientas especializadas para robótica y gráficos.

### 📌 Estructura del Código
El código se divide en los siguientes módulos:

- `finger.py`: Define la estructura de cada dedo con la convención de Denavit-Hartenberg.
- `robot.py`: Modela la mano robótica con tres dedos.
- `object.py`: Representa el objeto a manipular y sus puntos de contacto.
- `RobotAPI.py`: Implementa una API basada en **FastAPI** para el control remoto.
- `playground.py`: Espacio de pruebas para simulaciones.

### 📌 Proceso de Simulación
1. **Inicialización del Robot y Objeto:** Configuración inicial de los dedos y su posición en el espacio.  
2. **Cálculo de Cinemática:** Determinación de posiciones finales usando matrices de transformación.  
3. **Visualización:** Representación gráfica del sistema en 3D con `matplotlib`.  
4. **Interacción Web:** Uso de `FastAPI` para permitir comandos remotos.  

### 📌 API y Control Remoto
Se creó una API para modificar los movimientos del robot en tiempo real:

```python
import requests

url = "http://localhost:8000/{finger}"
params = {"link2": 1.0}
response = requests.get(url, params=params)
print(response.json())  # Expected output: {'newAngle': <calculated_angle>}
```

<br>

## 📊 Resultados  

La simulación logró una **manipulación precisa** del objeto, sin embargo, se presentaron desafíos en la implementación completa de las ecuaciones derivadas.  

📌 **Principales hallazgos:**  
- ✔️ Se logró modelar el contacto entre los dedos y el objeto con buena precisión.  
- ⚠️ Dificultades en la integración de ecuaciones dinámicas completas.  
- 🔄 Se recomienda mejorar la eficiencia computacional en el cálculo de cinemática inversa.  

🔗 **Video de la simulación:**  
[![Ver Video](https://img.youtube.com/vi/g31woEZeYF8/0.jpg)](https://www.youtube.com/watch?v=g31woEZeYF8)  


## 💡 Discusión y Futuro

### 📌 Mejoras propuestas:
- 🚀 **Optimización del modelo de cinemática inversa** para mejorar el rendimiento.
- 🖐️ **Implementación de sensores táctiles simulados** para ajustar la fuerza de agarre.
- 🤖 **Uso de aprendizaje automático** para mejorar la estabilidad del agarre en distintas condiciones.

---

## 📚 Referencias

1. 📖 M. T. Mason y J. K. Salisbury, *Robot Hands and the Mechanics of Manipulation*, MIT Press, 1985.
2. 📖 A. Bicchi y V. Kumar, *Robotic grasping and contact: A review*, IEEE ICRA, 2000.
3. 📖 J. J. Craig, *Introduction to Robotics: Mechanics and Control*, 4ta edición, Pearson, 2017.

---

## 🛠️ Instalación y Uso

### 📌 Requisitos:
- 🐍 **Python 3.10+**
- 🎮 **Unity con API de integración**
- 📦 `roboticstoolbox`, `spatialmath`, `FastAPI`, `matplotlib`

### 📌 Instalación:
```bash
pip install roboticstoolbox-python spatialmath matplotlib fastapi

## 🛠️ Debugging
Si experimentas problemas con la API, prueba lo siguiente:
- Verifica que todos los paquetes están instalados (`pip list`).
- Asegúrate de ejecutar `uvicorn RobotAPI:app --reload` para iniciar la API.
- Para probar manualmente la API, usa:
```bash
curl -X GET "http://127.0.0.1:8000/{finger}?link2=1.0"
