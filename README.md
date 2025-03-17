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

## 📖 Índice

1. [Introducción](#introducción)
2. [Fundamentos Matemáticos](#fundamentos-matemáticos)
   - [Ecuaciones del Robot](#ecuaciones-del-robot)
   - [Modelado del Contacto](#modelado-del-contacto)
3. [Cinemática](#cinemática)
   - [Cinemática Directa](#cinemática-directa)
   - [Cinemática Inversa](#cinemática-inversa)
4. [Modelos de Agarre](#modelos-de-agarre)
   - [Rodamiento y Deslizamiento](#rodamiento-y-deslizamiento)
5. [Implementación](#implementación)
   - [Estructura del Código](#estructura-del-código)
   - [Proceso de Simulación](#proceso-de-simulación)
6. [Resultados](#resultados)
7. [Discusión y Futuro](#discusión-y-futuro)
8. [Referencias](#referencias)
9. [Instalación y Uso](#instalación-y-uso)

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




---

## 🚀 **Installation & Setup**
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AldonDC/Robotic-Hand-Unity.git
cd Robotic-Hand-Unity
