# @title 🌍 Simulador Orbital con Tamaños y Escala Real
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import LineCollection
# from IPython.display import HTML
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# --- OPCIONES PRINCIPALES ---
modo_orbita = "Personalizada"  # @param ["Personalizada", "Órbita circular automática"]
tipo_cuerpo_central = "Sol"  # @param ["Tierra", "Marte", "Júpiter", "Sol", "Agujero negro", "Personalizado"]
tipo_satelite = "Júpiter"  # @param ["Tierra", "Marte", "Júpiter", "Personalizado"]
mostrar_animacion = True  # @param {type:"boolean"}
usar_gradiente_color = False  # @param {type:"boolean"}
formato_exportacion = "Ninguno"  # @param ["Ninguno", "GIF", "MP4"]
activar_friccion = False  # @param {type:"boolean"}

# --- PARÁMETROS DE ANIMACIÓN ---
tiempo_total = 27000  # @param {type:"number"}  # segundos
dt = 8.0  # @param {type:"number"}  # paso temporal en segundos
salto_de_frames = 6  # @param {type:"number"}  # cada cuántos frames se renderiza la animación
velocidad_animacion = 15  # @param {type:"number"}  # intervalo de animación en milisegundos

# --- PARÁMETROS PERSONALIZADOS (solo si se elige "Personalizado") ---
masa_personalizada = 5.972e24  # @param {type:"number"}  # en kg
radio_personalizado = 6371  # @param {type:"number"}  # en km
posicion_inicial_x = 1200000  # @param {type:"number"}  # en km
posicion_inicial_y = 0.0  # @param {type:"number"}
velocidad_inicial_x = 0.0  # @param {type:"number"}  # en m/s
velocidad_inicial_y = 350000.0  # @param {type:"number"}  # en m/s
radio_satelite_personalizado = 1.0  # @param {type:"number"}  # en km

# --- CUERPOS CENTRALES ---
cuerpos_centrales = {
    "Tierra": {"masa": 5.972e24, "radio": 6_371, "pos": (7_000, 0), "vel": (0, 7_500)},
    "Marte": {"masa": 6.39e23, "radio": 3_390, "pos": (6_000, 0), "vel": (0, 6_500)},
    "Júpiter": {"masa": 1.898e27, "radio": 69_911, "pos": (75_000, 0), "vel": (0, 13_000)},
    "Sol": {"masa": 1.989e30, "radio": 696_340, "pos": (1_500_000, 0), "vel": (0, 29_800)},
    "Agujero negro": {"masa": 5e30, "radio": 10, "pos": (10_000, 0), "vel": (0, 25_000)}
}

satelites = {
    "Tierra": {"radio": 6_371},
    "Marte": {"radio": 3_390},
    "Júpiter": {"radio": 69_911}
}

# --- SELECCIÓN DE PARÁMETROS ---
if tipo_cuerpo_central == "Personalizado":
    masa_central = masa_personalizada
    radio_del_cuerpo = radio_personalizado
else:
    planeta = cuerpos_centrales[tipo_cuerpo_central]
    masa_central = planeta["masa"]
    radio_del_cuerpo = planeta["radio"]

# (esta parte se movió arriba con G y antes del uso de radio_satelite)

# Radio del satélite
if tipo_satelite == "Personalizado":
    radio_satelite = radio_satelite_personalizado
else:
    radio_satelite = satelites[tipo_satelite]["radio"]

# Determinar condiciones iniciales según modo seleccionado
G = 6.674e-11  # constante de gravitación
if modo_orbita == "Órbita circular automática":
    # Determinar una órbita circular segura a una distancia razonable (por ejemplo 3 radios planetarios)
    r_circular = (radio_del_cuerpo + radio_satelite + 1000) * 1000  # en metros
    x = r_circular
    y = 0
    vx = 0
    vy = np.sqrt(G * masa_central / r_circular)
else:
    x = posicion_inicial_x * 1_000
    y = posicion_inicial_y * 1_000
    vx = velocidad_inicial_x
    vy = velocidad_inicial_y

# --- PARÁMETROS DE SIMULACIÓN ---
pasos = int(tiempo_total / dt)
G = 6.674e-11
x_list, y_list = [x], [y]
vel_list, dist_list = [], []
colision = False

# --- FUNCIONES ---
def aceleracion(x, y):
    r = np.sqrt(x**2 + y**2)
    ax = -G * masa_central * x / r**3
    ay = -G * masa_central * y / r**3
    return ax, ay

for _ in range(pasos):
    r = np.sqrt(x**2 + y**2)
    if r <= (radio_del_cuerpo + radio_satelite) * 1_000:
        print(f"☄️ ¡Colisión! El objeto impactó a r = {r / 1_000:.2f} km")
        colision = True
        break

    ax1, ay1 = aceleracion(x, y)
    k1vx, k1vy = ax1, ay1
    k1x, k1y = vx, vy

    x2 = x + 0.5 * dt * k1x
    y2 = y + 0.5 * dt * k1y
    vx2 = vx + 0.5 * dt * k1vx
    vy2 = vy + 0.5 * dt * k1vy
    ax2, ay2 = aceleracion(x2, y2)
    k2vx, k2vy = ax2, ay2
    k2x, k2y = vx2, vy2

    x3 = x + 0.5 * dt * k2x
    y3 = y + 0.5 * dt * k2y
    vx3 = vx + 0.5 * dt * k2vx
    vy3 = vy + 0.5 * dt * k2vy
    ax3, ay3 = aceleracion(x3, y3)
    k3vx, k3vy = ax3, ay3
    k3x, k3y = vx3, vy3

    x4 = x + dt * k3x
    y4 = y + dt * k3y
    vx4 = vx + dt * k3vx
    vy4 = vy + dt * k3vy
    ax4, ay4 = aceleracion(x4, y4)
    k4vx, k4vy = ax4, ay4
    k4x, k4y = vx4, vy4

    x += (dt / 6.0) * (k1x + 2*k2x + 2*k3x + k4x)
    y += (dt / 6.0) * (k1y + 2*k2y + 2*k3y + k4y)
    vx += (dt / 6.0) * (k1vx + 2*k2vx + 2*k3vx + k4vx)
    vy += (dt / 6.0) * (k1vy + 2*k2vy + 2*k3vy + k4vy)

    if activar_friccion:
        vx *= 0.9999
        vy *= 0.9999

    x_list.append(x)
    y_list.append(y)
    vel_list.append(np.sqrt(vx**2 + vy**2))
    dist_list.append(np.sqrt(x**2 + y**2))

# --- ANIMACIÓN Y GRÁFICO FINAL ---

# --- INFORMES ORBITALES ---
if colision:
    print(f"☄️ El satélite colisionó con el cuerpo central tras {len(x_list) * dt:.2f} s.")
else:
    r0 = np.sqrt(x_list[0]**2 + y_list[0]**2)
    E = 0.5 * (vx**2 + vy**2) - G * masa_central / r0
    print("🌀 Órbita estable." if E < 0 else "🚀 Escape." if E > 0 else "🟡 Órbita parabólica.", f"Energía total = {E:.2e} J")
    if len(dist_list) > 1:
        r_min = np.min(dist_list)
        r_max = np.max(dist_list)
        a = 0.5 * (r_max + r_min)
        periodo = 2 * np.pi * np.sqrt(a**3 / (G * masa_central))
        excentricidad = (r_max - r_min) / (r_max + r_min)
        print(f"📏 Distancia mínima: {r_min/1_000:.2f} km")
        print(f"📐 Distancia máxima: {r_max/1_000:.2f} km")
        print(f"💠 Excentricidad: {excentricidad:.3f}")
        print(f"🕒 Período estimado: {periodo:.2f} s")
x_km = np.array(x_list) / 1000
y_km = np.array(y_list) / 1000
fig, ax = plt.subplots(figsize=(8, 8))

# Escalado visual amplio
margin_x = 0.5 * (x_km.max() - x_km.min())
margin_y = 0.5 * (y_km.max() - y_km.min())

# Asegurar que haya margen visible aunque solo haya un punto (por ejemplo, colisión al primer paso)
if margin_x == 0:
    margin_x = 1
if margin_y == 0:
    margin_y = 1
trayectoria_max = max(np.abs(x_km).max(), np.abs(y_km).max())
vista_max = max(radio_del_cuerpo * 1.2, trayectoria_max * 1.1)
ax.set_xlim(-vista_max, vista_max)
ax.set_ylim(-vista_max, vista_max)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title("Trayectoria Orbital 2D")
ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")

if usar_gradiente_color and len(vel_list) > 1 and len(vel_list) == len(x_km) - 1:
    velocities = np.array(vel_list)
    points = np.array([x_km, y_km]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    norm = mcolors.Normalize(vmin=velocities.min(), vmax=velocities.max())
    lc = LineCollection(segments, cmap='plasma', norm=norm)
    lc.set_array(velocities)
    lc.set_linewidth(2)
    ax.add_collection(lc)
else:
    ax.plot(x_km, y_km, 'b-', label='Trayectoria')

ax.plot(x_km[-1], y_km[-1], 'ro', label='Satélite')
ax.add_patch(Circle((0, 0), radius=radio_del_cuerpo, color='goldenrod', label='Cuerpo central'))
ax.add_patch(Circle((x_km[-1], y_km[-1]), radius=radio_satelite, color='red', alpha=0.5, label='Satélite físico'))
ax.legend()
plt.show()

# --- ANIMACIÓN ---
if mostrar_animacion:
    from matplotlib import animation, rc
    rc('animation', html='jshtml')
    fig2, ax2 = plt.subplots(figsize=(8,8))
    ax2.set_xlim(x_km.min() - margin_x, x_km.max() + margin_x)
    ax2.set_ylim(y_km.min() - margin_y, y_km.max() + margin_y)
    ax2.set_aspect('equal')
    ax2.grid(True)
    ax2.set_title("Simulación orbital animada")
    ax2.set_xlabel("X (km)")
    ax2.set_ylabel("Y (km)")

    if usar_gradiente_color and len(vel_list) == len(x_km) - 1:
        norm = mcolors.Normalize(vmin=min(vel_list), vmax=max(vel_list))
        cmap = plt.get_cmap('plasma')
    linea, = ax2.plot([], [], '-', lw=2)
    sat_patch = Circle((x_km[0], y_km[0]), radius=radio_satelite, color='red', alpha=0.5)
    ax2.add_patch(sat_patch)
    punto, = ax2.plot([], [], 'ro', markersize=5)
    estrella = Circle((0, 0), radius=radio_del_cuerpo, color='goldenrod', label='Cuerpo central')
    ax2.add_patch(estrella)

    def init():
        linea.set_data([], [])
        punto.set_data([], [])
        sat_patch.center = (x_km[0], y_km[0])
        return linea, punto, estrella, sat_patch

    def update(frame):
        i = frame * salto_de_frames
        if i < 2:
            return linea, punto, estrella, sat_patch
        i = min(i, len(x_km) - 1)
        if usar_gradiente_color and len(vel_list) == len(x_km) - 1:
            color = cmap(norm(vel_list[i]))
            linea.set_color(color)
        linea.set_data(x_km[:i+1], y_km[:i+1])
        punto.set_data([x_km[i]], [y_km[i]])
        sat_patch.center = (x_km[i], y_km[i])
        return linea, punto, estrella, sat_patch

    frames_total = len(x_km) // salto_de_frames
    anim = animation.FuncAnimation(fig2, update, init_func=init, frames=frames_total, interval=velocidad_animacion, blit=True)

    if formato_exportacion == "GIF":
        anim.save("orbita.gif", writer="pillow")
    elif formato_exportacion == "MP4":
        anim.save("orbita.mp4", writer="ffmpeg")
    else:
        st.video("orbita.mp4")   # si exportás como MP4
    plt.close(fig2)


#-------------------------------------------------A----------------------------------A-------------------------------------
#------------------------------------------------AAA--------------------------------AAA--------------------------------------
#-------------------------------------------------A----------------------------------A-------------------------------------

if len(x_km) == 1:
    # Repetimos un segundo punto para que el gráfico tenga escala
    x_km = np.append(x_km, x_km[0] + 1)
    y_km = np.append(y_km, y_km[0] + 1)

ax.plot(x_km[-1], y_km[-1], 'ro', label='Satélite')
ax.add_patch(Circle((0, 0), radius=radio_del_cuerpo, color='goldenrod', label='Cuerpo central'))
ax.add_patch(Circle((x_km[-1], y_km[-1]), radius=radio_satelite*0.01, color='gray', alpha=0.5))
ax.legend()
plt.show()

if colision:
    print(f"⏱️ Tiempo hasta colisión: {len(x_list)*dt:.2f} s")

if colision:
    print(f"☄️ El satélite colisionó con el cuerpo central tras {len(x_list) * dt:.2f} s.")
else:
    r0 = np.sqrt(x_list[0]**2 + y_list[0]**2)
    E = 0.5 * (vx**2 + vy**2) - G * masa_central / r0
    print("🌀 Órbita estable." if E < 0 else "🚀 Escape." if E > 0 else "🟡 Órbita parabólica.", f"Energía total = {E:.2e} J")
    if len(dist_list) > 1:
        r_min = np.min(dist_list)
        r_max = np.max(dist_list)
        a = 0.5 * (r_max + r_min)
        periodo = 2 * np.pi * np.sqrt(a**3 / (G * masa_central))
        excentricidad = (r_max - r_min) / (r_max + r_min)
        print(f"📏 Distancia mínima: {r_min/1_000:.2f} km")
        print(f"📐 Distancia máxima: {r_max/1_000:.2f} km")
        print(f"💠 Excentricidad: {excentricidad:.3f}")
        print(f"🕒 Período estimado: {periodo:.2f} s")
