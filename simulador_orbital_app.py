{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red245\green245\blue245;\red0\green0\blue0;
\red131\green0\blue165;\red144\green1\blue18;\red0\green0\blue255;\red19\green85\blue52;\red31\green99\blue128;
\red86\green65\blue25;\red0\green0\blue109;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c96863\c96863\c96863;\cssrgb\c0\c0\c0;
\cssrgb\c59216\c13725\c70588;\cssrgb\c63922\c8235\c8235;\cssrgb\c0\c0\c100000;\cssrgb\c6667\c40000\c26667;\cssrgb\c14510\c46275\c57647;
\cssrgb\c41569\c32157\c12941;\cssrgb\c0\c6275\c50196;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # @title \uc0\u55356 \u57101  Simulador Orbital con Tama\'f1os y Escala Real\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 import\cf0 \strokec4  numpy \cf5 \strokec5 as\cf0 \strokec4  np\cb1 \
\cf5 \cb3 \strokec5 import\cf0 \strokec4  matplotlib.pyplot \cf5 \strokec5 as\cf0 \strokec4  plt\cb1 \
\cf5 \cb3 \strokec5 from\cf0 \strokec4  matplotlib.patches \cf5 \strokec5 import\cf0 \strokec4  Circle\cb1 \
\cf5 \cb3 \strokec5 from\cf0 \strokec4  matplotlib.collections \cf5 \strokec5 import\cf0 \strokec4  LineCollection\cb1 \
\cf5 \cb3 \strokec5 from\cf0 \strokec4  IPython.display \cf5 \strokec5 import\cf0 \strokec4  HTML\cb1 \
\cf5 \cb3 \strokec5 import\cf0 \strokec4  matplotlib.cm \cf5 \strokec5 as\cf0 \strokec4  cm\cb1 \
\cf5 \cb3 \strokec5 import\cf0 \strokec4  matplotlib.colors \cf5 \strokec5 as\cf0 \strokec4  mcolors\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # --- OPCIONES PRINCIPALES ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 modo_orbita = \cf6 \strokec6 "Personalizada"\cf0 \strokec4   \cf2 \strokec2 # @param ["Personalizada", "\'d3rbita circular autom\'e1tica"]\cf0 \cb1 \strokec4 \
\cb3 tipo_cuerpo_central = \cf6 \strokec6 "Sol"\cf0 \strokec4   \cf2 \strokec2 # @param ["Tierra", "Marte", "J\'fapiter", "Sol", "Agujero negro", "Personalizado"]\cf0 \cb1 \strokec4 \
\cb3 tipo_satelite = \cf6 \strokec6 "J\'fapiter"\cf0 \strokec4   \cf2 \strokec2 # @param ["Tierra", "Marte", "J\'fapiter", "Personalizado"]\cf0 \cb1 \strokec4 \
\cb3 mostrar_animacion = \cf7 \strokec7 True\cf0 \strokec4   \cf2 \strokec2 # @param \{type:"boolean"\}\cf0 \cb1 \strokec4 \
\cb3 usar_gradiente_color = \cf7 \strokec7 False\cf0 \strokec4   \cf2 \strokec2 # @param \{type:"boolean"\}\cf0 \cb1 \strokec4 \
\cb3 formato_exportacion = \cf6 \strokec6 "Ninguno"\cf0 \strokec4   \cf2 \strokec2 # @param ["Ninguno", "GIF", "MP4"]\cf0 \cb1 \strokec4 \
\cb3 activar_friccion = \cf7 \strokec7 False\cf0 \strokec4   \cf2 \strokec2 # @param \{type:"boolean"\}\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # --- PAR\'c1METROS DE ANIMACI\'d3N ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 tiempo_total = \cf8 \strokec8 27000\cf0 \strokec4   \cf2 \strokec2 # @param \{type:"number"\}  # segundos\cf0 \cb1 \strokec4 \
\cb3 dt = \cf8 \strokec8 8.0\cf0 \strokec4   \cf2 \strokec2 # @param \{type:"number"\}  # paso temporal en segundos\cf0 \cb1 \strokec4 \
\cb3 salto_de_frames = \cf8 \strokec8 6\cf0 \strokec4   \cf2 \strokec2 # @param \{type:"number"\}  # cada cu\'e1ntos frames se renderiza la animaci\'f3n\cf0 \cb1 \strokec4 \
\cb3 velocidad_animacion = \cf8 \strokec8 15\cf0 \strokec4   \cf2 \strokec2 # @param \{type:"number"\}  # intervalo de animaci\'f3n en milisegundos\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # --- PAR\'c1METROS PERSONALIZADOS (solo si se elige "Personalizado") ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 masa_personalizada = \cf8 \strokec8 5.972e24\cf0 \strokec4   \cf2 \strokec2 # @param \{type:"number"\}  # en kg\cf0 \cb1 \strokec4 \
\cb3 radio_personalizado = \cf8 \strokec8 6371\cf0 \strokec4   \cf2 \strokec2 # @param \{type:"number"\}  # en km\cf0 \cb1 \strokec4 \
\cb3 posicion_inicial_x = \cf8 \strokec8 1200000\cf0 \strokec4   \cf2 \strokec2 # @param \{type:"number"\}  # en km\cf0 \cb1 \strokec4 \
\cb3 posicion_inicial_y = \cf8 \strokec8 0.0\cf0 \strokec4   \cf2 \strokec2 # @param \{type:"number"\}\cf0 \cb1 \strokec4 \
\cb3 velocidad_inicial_x = \cf8 \strokec8 0.0\cf0 \strokec4   \cf2 \strokec2 # @param \{type:"number"\}  # en m/s\cf0 \cb1 \strokec4 \
\cb3 velocidad_inicial_y = \cf8 \strokec8 350000.0\cf0 \strokec4   \cf2 \strokec2 # @param \{type:"number"\}  # en m/s\cf0 \cb1 \strokec4 \
\cb3 radio_satelite_personalizado = \cf8 \strokec8 1.0\cf0 \strokec4   \cf2 \strokec2 # @param \{type:"number"\}  # en km\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # --- CUERPOS CENTRALES ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 cuerpos_centrales = \{\cb1 \
\cb3     \cf6 \strokec6 "Tierra"\cf0 \strokec4 : \{\cf6 \strokec6 "masa"\cf0 \strokec4 : \cf8 \strokec8 5.972e24\cf0 \strokec4 , \cf6 \strokec6 "radio"\cf0 \strokec4 : \cf8 \strokec8 6_371\cf0 \strokec4 , \cf6 \strokec6 "pos"\cf0 \strokec4 : (\cf8 \strokec8 7_000\cf0 \strokec4 , \cf8 \strokec8 0\cf0 \strokec4 ), \cf6 \strokec6 "vel"\cf0 \strokec4 : (\cf8 \strokec8 0\cf0 \strokec4 , \cf8 \strokec8 7_500\cf0 \strokec4 )\},\cb1 \
\cb3     \cf6 \strokec6 "Marte"\cf0 \strokec4 : \{\cf6 \strokec6 "masa"\cf0 \strokec4 : \cf8 \strokec8 6.39e23\cf0 \strokec4 , \cf6 \strokec6 "radio"\cf0 \strokec4 : \cf8 \strokec8 3_390\cf0 \strokec4 , \cf6 \strokec6 "pos"\cf0 \strokec4 : (\cf8 \strokec8 6_000\cf0 \strokec4 , \cf8 \strokec8 0\cf0 \strokec4 ), \cf6 \strokec6 "vel"\cf0 \strokec4 : (\cf8 \strokec8 0\cf0 \strokec4 , \cf8 \strokec8 6_500\cf0 \strokec4 )\},\cb1 \
\cb3     \cf6 \strokec6 "J\'fapiter"\cf0 \strokec4 : \{\cf6 \strokec6 "masa"\cf0 \strokec4 : \cf8 \strokec8 1.898e27\cf0 \strokec4 , \cf6 \strokec6 "radio"\cf0 \strokec4 : \cf8 \strokec8 69_911\cf0 \strokec4 , \cf6 \strokec6 "pos"\cf0 \strokec4 : (\cf8 \strokec8 75_000\cf0 \strokec4 , \cf8 \strokec8 0\cf0 \strokec4 ), \cf6 \strokec6 "vel"\cf0 \strokec4 : (\cf8 \strokec8 0\cf0 \strokec4 , \cf8 \strokec8 13_000\cf0 \strokec4 )\},\cb1 \
\cb3     \cf6 \strokec6 "Sol"\cf0 \strokec4 : \{\cf6 \strokec6 "masa"\cf0 \strokec4 : \cf8 \strokec8 1.989e30\cf0 \strokec4 , \cf6 \strokec6 "radio"\cf0 \strokec4 : \cf8 \strokec8 696_340\cf0 \strokec4 , \cf6 \strokec6 "pos"\cf0 \strokec4 : (\cf8 \strokec8 1_500_000\cf0 \strokec4 , \cf8 \strokec8 0\cf0 \strokec4 ), \cf6 \strokec6 "vel"\cf0 \strokec4 : (\cf8 \strokec8 0\cf0 \strokec4 , \cf8 \strokec8 29_800\cf0 \strokec4 )\},\cb1 \
\cb3     \cf6 \strokec6 "Agujero negro"\cf0 \strokec4 : \{\cf6 \strokec6 "masa"\cf0 \strokec4 : \cf8 \strokec8 5e30\cf0 \strokec4 , \cf6 \strokec6 "radio"\cf0 \strokec4 : \cf8 \strokec8 10\cf0 \strokec4 , \cf6 \strokec6 "pos"\cf0 \strokec4 : (\cf8 \strokec8 10_000\cf0 \strokec4 , \cf8 \strokec8 0\cf0 \strokec4 ), \cf6 \strokec6 "vel"\cf0 \strokec4 : (\cf8 \strokec8 0\cf0 \strokec4 , \cf8 \strokec8 25_000\cf0 \strokec4 )\}\cb1 \
\cb3 \}\cb1 \
\
\cb3 satelites = \{\cb1 \
\cb3     \cf6 \strokec6 "Tierra"\cf0 \strokec4 : \{\cf6 \strokec6 "radio"\cf0 \strokec4 : \cf8 \strokec8 6_371\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 "Marte"\cf0 \strokec4 : \{\cf6 \strokec6 "radio"\cf0 \strokec4 : \cf8 \strokec8 3_390\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 "J\'fapiter"\cf0 \strokec4 : \{\cf6 \strokec6 "radio"\cf0 \strokec4 : \cf8 \strokec8 69_911\cf0 \strokec4 \}\cb1 \
\cb3 \}\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # --- SELECCI\'d3N DE PAR\'c1METROS ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf0 \strokec4  tipo_cuerpo_central == \cf6 \strokec6 "Personalizado"\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     masa_central = masa_personalizada\cb1 \
\cb3     radio_del_cuerpo = radio_personalizado\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 else\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     planeta = cuerpos_centrales[tipo_cuerpo_central]\cb1 \
\cb3     masa_central = planeta[\cf6 \strokec6 "masa"\cf0 \strokec4 ]\cb1 \
\cb3     radio_del_cuerpo = planeta[\cf6 \strokec6 "radio"\cf0 \strokec4 ]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # (esta parte se movi\'f3 arriba con G y antes del uso de radio_satelite)\cf0 \cb1 \strokec4 \
\
\cf2 \cb3 \strokec2 # Radio del sat\'e9lite\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf0 \strokec4  tipo_satelite == \cf6 \strokec6 "Personalizado"\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     radio_satelite = radio_satelite_personalizado\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 else\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     radio_satelite = satelites[tipo_satelite][\cf6 \strokec6 "radio"\cf0 \strokec4 ]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Determinar condiciones iniciales seg\'fan modo seleccionado\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 G = \cf8 \strokec8 6.674e-11\cf0 \strokec4   \cf2 \strokec2 # constante de gravitaci\'f3n\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf0 \strokec4  modo_orbita == \cf6 \strokec6 "\'d3rbita circular autom\'e1tica"\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 # Determinar una \'f3rbita circular segura a una distancia razonable (por ejemplo 3 radios planetarios)\cf0 \cb1 \strokec4 \
\cb3     r_circular = (radio_del_cuerpo + radio_satelite + \cf8 \strokec8 1000\cf0 \strokec4 ) * \cf8 \strokec8 1000\cf0 \strokec4   \cf2 \strokec2 # en metros\cf0 \cb1 \strokec4 \
\cb3     x = r_circular\cb1 \
\cb3     y = \cf8 \strokec8 0\cf0 \cb1 \strokec4 \
\cb3     vx = \cf8 \strokec8 0\cf0 \cb1 \strokec4 \
\cb3     vy = np.sqrt(G * masa_central / r_circular)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 else\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     x = posicion_inicial_x * \cf8 \strokec8 1_000\cf0 \cb1 \strokec4 \
\cb3     y = posicion_inicial_y * \cf8 \strokec8 1_000\cf0 \cb1 \strokec4 \
\cb3     vx = velocidad_inicial_x\cb1 \
\cb3     vy = velocidad_inicial_y\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # --- PAR\'c1METROS DE SIMULACI\'d3N ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 pasos = \cf9 \strokec9 int\cf0 \strokec4 (tiempo_total / dt)\cb1 \
\cb3 G = \cf8 \strokec8 6.674e-11\cf0 \cb1 \strokec4 \
\cb3 x_list, y_list = [x], [y]\cb1 \
\cb3 vel_list, dist_list = [], []\cb1 \
\cb3 colision = \cf7 \strokec7 False\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # --- FUNCIONES ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf0 \strokec4  \cf10 \strokec10 aceleracion\cf0 \strokec4 (\cf11 \strokec11 x\cf0 \strokec4 , \cf11 \strokec11 y\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     r = np.sqrt(x**\cf8 \strokec8 2\cf0 \strokec4  + y**\cf8 \strokec8 2\cf0 \strokec4 )\cb1 \
\cb3     ax = -G * masa_central * x / r**\cf8 \strokec8 3\cf0 \cb1 \strokec4 \
\cb3     ay = -G * masa_central * y / r**\cf8 \strokec8 3\cf0 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 return\cf0 \strokec4  ax, ay\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 for\cf0 \strokec4  _ \cf7 \strokec7 in\cf0 \strokec4  \cf10 \strokec10 range\cf0 \strokec4 (pasos):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     r = np.sqrt(x**\cf8 \strokec8 2\cf0 \strokec4  + y**\cf8 \strokec8 2\cf0 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 if\cf0 \strokec4  r <= (radio_del_cuerpo + radio_satelite) * \cf8 \strokec8 1_000\cf0 \strokec4 :\cb1 \
\cb3         \cf10 \strokec10 print\cf0 \strokec4 (\cf7 \strokec7 f\cf6 \strokec6 "\uc0\u9732 \u65039  \'a1Colisi\'f3n! El objeto impact\'f3 a r = \cf0 \strokec4 \{r / \cf8 \strokec8 1_000:.2f\cf0 \strokec4 \}\cf6 \strokec6  km"\cf0 \strokec4 )\cb1 \
\cb3         colision = \cf7 \strokec7 True\cf0 \cb1 \strokec4 \
\cb3         \cf5 \strokec5 break\cf0 \cb1 \strokec4 \
\
\cb3     ax1, ay1 = aceleracion(x, y)\cb1 \
\cb3     k1vx, k1vy = ax1, ay1\cb1 \
\cb3     k1x, k1y = vx, vy\cb1 \
\
\cb3     x2 = x + \cf8 \strokec8 0.5\cf0 \strokec4  * dt * k1x\cb1 \
\cb3     y2 = y + \cf8 \strokec8 0.5\cf0 \strokec4  * dt * k1y\cb1 \
\cb3     vx2 = vx + \cf8 \strokec8 0.5\cf0 \strokec4  * dt * k1vx\cb1 \
\cb3     vy2 = vy + \cf8 \strokec8 0.5\cf0 \strokec4  * dt * k1vy\cb1 \
\cb3     ax2, ay2 = aceleracion(x2, y2)\cb1 \
\cb3     k2vx, k2vy = ax2, ay2\cb1 \
\cb3     k2x, k2y = vx2, vy2\cb1 \
\
\cb3     x3 = x + \cf8 \strokec8 0.5\cf0 \strokec4  * dt * k2x\cb1 \
\cb3     y3 = y + \cf8 \strokec8 0.5\cf0 \strokec4  * dt * k2y\cb1 \
\cb3     vx3 = vx + \cf8 \strokec8 0.5\cf0 \strokec4  * dt * k2vx\cb1 \
\cb3     vy3 = vy + \cf8 \strokec8 0.5\cf0 \strokec4  * dt * k2vy\cb1 \
\cb3     ax3, ay3 = aceleracion(x3, y3)\cb1 \
\cb3     k3vx, k3vy = ax3, ay3\cb1 \
\cb3     k3x, k3y = vx3, vy3\cb1 \
\
\cb3     x4 = x + dt * k3x\cb1 \
\cb3     y4 = y + dt * k3y\cb1 \
\cb3     vx4 = vx + dt * k3vx\cb1 \
\cb3     vy4 = vy + dt * k3vy\cb1 \
\cb3     ax4, ay4 = aceleracion(x4, y4)\cb1 \
\cb3     k4vx, k4vy = ax4, ay4\cb1 \
\cb3     k4x, k4y = vx4, vy4\cb1 \
\
\cb3     x += (dt / \cf8 \strokec8 6.0\cf0 \strokec4 ) * (k1x + \cf8 \strokec8 2\cf0 \strokec4 *k2x + \cf8 \strokec8 2\cf0 \strokec4 *k3x + k4x)\cb1 \
\cb3     y += (dt / \cf8 \strokec8 6.0\cf0 \strokec4 ) * (k1y + \cf8 \strokec8 2\cf0 \strokec4 *k2y + \cf8 \strokec8 2\cf0 \strokec4 *k3y + k4y)\cb1 \
\cb3     vx += (dt / \cf8 \strokec8 6.0\cf0 \strokec4 ) * (k1vx + \cf8 \strokec8 2\cf0 \strokec4 *k2vx + \cf8 \strokec8 2\cf0 \strokec4 *k3vx + k4vx)\cb1 \
\cb3     vy += (dt / \cf8 \strokec8 6.0\cf0 \strokec4 ) * (k1vy + \cf8 \strokec8 2\cf0 \strokec4 *k2vy + \cf8 \strokec8 2\cf0 \strokec4 *k3vy + k4vy)\cb1 \
\
\cb3     \cf5 \strokec5 if\cf0 \strokec4  activar_friccion:\cb1 \
\cb3         vx *= \cf8 \strokec8 0.9999\cf0 \cb1 \strokec4 \
\cb3         vy *= \cf8 \strokec8 0.9999\cf0 \cb1 \strokec4 \
\
\cb3     x_list.append(x)\cb1 \
\cb3     y_list.append(y)\cb1 \
\cb3     vel_list.append(np.sqrt(vx**\cf8 \strokec8 2\cf0 \strokec4  + vy**\cf8 \strokec8 2\cf0 \strokec4 ))\cb1 \
\cb3     dist_list.append(np.sqrt(x**\cf8 \strokec8 2\cf0 \strokec4  + y**\cf8 \strokec8 2\cf0 \strokec4 ))\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # --- ANIMACI\'d3N Y GR\'c1FICO FINAL ---\cf0 \cb1 \strokec4 \
\
\cf2 \cb3 \strokec2 # --- INFORMES ORBITALES ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf0 \strokec4  colision:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf10 \strokec10 print\cf0 \strokec4 (\cf7 \strokec7 f\cf6 \strokec6 "\uc0\u9732 \u65039  El sat\'e9lite colision\'f3 con el cuerpo central tras \cf0 \strokec4 \{\cf10 \strokec10 len\cf0 \strokec4 (x_list) * dt\cf8 \strokec8 :.2f\cf0 \strokec4 \}\cf6 \strokec6  s."\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 else\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     r0 = np.sqrt(x_list[\cf8 \strokec8 0\cf0 \strokec4 ]**\cf8 \strokec8 2\cf0 \strokec4  + y_list[\cf8 \strokec8 0\cf0 \strokec4 ]**\cf8 \strokec8 2\cf0 \strokec4 )\cb1 \
\cb3     E = \cf8 \strokec8 0.5\cf0 \strokec4  * (vx**\cf8 \strokec8 2\cf0 \strokec4  + vy**\cf8 \strokec8 2\cf0 \strokec4 ) - G * masa_central / r0\cb1 \
\cb3     \cf10 \strokec10 print\cf0 \strokec4 (\cf6 \strokec6 "\uc0\u55356 \u57088  \'d3rbita estable."\cf0 \strokec4  \cf5 \strokec5 if\cf0 \strokec4  E < \cf8 \strokec8 0\cf0 \strokec4  \cf5 \strokec5 else\cf0 \strokec4  \cf6 \strokec6 "\uc0\u55357 \u56960  Escape."\cf0 \strokec4  \cf5 \strokec5 if\cf0 \strokec4  E > \cf8 \strokec8 0\cf0 \strokec4  \cf5 \strokec5 else\cf0 \strokec4  \cf6 \strokec6 "\uc0\u55357 \u57313  \'d3rbita parab\'f3lica."\cf0 \strokec4 , \cf7 \strokec7 f\cf6 \strokec6 "Energ\'eda total = \cf0 \strokec4 \{E\cf8 \strokec8 :.2e\cf0 \strokec4 \}\cf6 \strokec6  J"\cf0 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 if\cf0 \strokec4  \cf10 \strokec10 len\cf0 \strokec4 (dist_list) > \cf8 \strokec8 1\cf0 \strokec4 :\cb1 \
\cb3         r_min = np.\cf10 \strokec10 min\cf0 \strokec4 (dist_list)\cb1 \
\cb3         r_max = np.\cf10 \strokec10 max\cf0 \strokec4 (dist_list)\cb1 \
\cb3         a = \cf8 \strokec8 0.5\cf0 \strokec4  * (r_max + r_min)\cb1 \
\cb3         periodo = \cf8 \strokec8 2\cf0 \strokec4  * np.pi * np.sqrt(a**\cf8 \strokec8 3\cf0 \strokec4  / (G * masa_central))\cb1 \
\cb3         excentricidad = (r_max - r_min) / (r_max + r_min)\cb1 \
\cb3         \cf10 \strokec10 print\cf0 \strokec4 (\cf7 \strokec7 f\cf6 \strokec6 "\uc0\u55357 \u56527  Distancia m\'ednima: \cf0 \strokec4 \{r_min/\cf8 \strokec8 1_000:.2f\cf0 \strokec4 \}\cf6 \strokec6  km"\cf0 \strokec4 )\cb1 \
\cb3         \cf10 \strokec10 print\cf0 \strokec4 (\cf7 \strokec7 f\cf6 \strokec6 "\uc0\u55357 \u56528  Distancia m\'e1xima: \cf0 \strokec4 \{r_max/\cf8 \strokec8 1_000:.2f\cf0 \strokec4 \}\cf6 \strokec6  km"\cf0 \strokec4 )\cb1 \
\cb3         \cf10 \strokec10 print\cf0 \strokec4 (\cf7 \strokec7 f\cf6 \strokec6 "\uc0\u55357 \u56480  Excentricidad: \cf0 \strokec4 \{excentricidad\cf8 \strokec8 :.3f\cf0 \strokec4 \}\cf6 \strokec6 "\cf0 \strokec4 )\cb1 \
\cb3         \cf10 \strokec10 print\cf0 \strokec4 (\cf7 \strokec7 f\cf6 \strokec6 "\uc0\u55357 \u56658  Per\'edodo estimado: \cf0 \strokec4 \{periodo\cf8 \strokec8 :.2f\cf0 \strokec4 \}\cf6 \strokec6  s"\cf0 \strokec4 )\cb1 \
\cb3 x_km = np.array(x_list) / \cf8 \strokec8 1000\cf0 \cb1 \strokec4 \
\cb3 y_km = np.array(y_list) / \cf8 \strokec8 1000\cf0 \cb1 \strokec4 \
\cb3 fig, ax = plt.subplots(figsize=(\cf8 \strokec8 8\cf0 \strokec4 , \cf8 \strokec8 8\cf0 \strokec4 ))\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Escalado visual amplio\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 margin_x = \cf8 \strokec8 0.5\cf0 \strokec4  * (x_km.\cf10 \strokec10 max\cf0 \strokec4 () - x_km.\cf10 \strokec10 min\cf0 \strokec4 ())\cb1 \
\cb3 margin_y = \cf8 \strokec8 0.5\cf0 \strokec4  * (y_km.\cf10 \strokec10 max\cf0 \strokec4 () - y_km.\cf10 \strokec10 min\cf0 \strokec4 ())\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Asegurar que haya margen visible aunque solo haya un punto (por ejemplo, colisi\'f3n al primer paso)\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf0 \strokec4  margin_x == \cf8 \strokec8 0\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     margin_x = \cf8 \strokec8 1\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf0 \strokec4  margin_y == \cf8 \strokec8 0\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     margin_y = \cf8 \strokec8 1\cf0 \cb1 \strokec4 \
\cb3 trayectoria_max = \cf10 \strokec10 max\cf0 \strokec4 (np.\cf10 \strokec10 abs\cf0 \strokec4 (x_km).\cf10 \strokec10 max\cf0 \strokec4 (), np.\cf10 \strokec10 abs\cf0 \strokec4 (y_km).\cf10 \strokec10 max\cf0 \strokec4 ())\cb1 \
\cb3 vista_max = \cf10 \strokec10 max\cf0 \strokec4 (radio_del_cuerpo * \cf8 \strokec8 1.2\cf0 \strokec4 , trayectoria_max * \cf8 \strokec8 1.1\cf0 \strokec4 )\cb1 \
\cb3 ax.set_xlim(-vista_max, vista_max)\cb1 \
\cb3 ax.set_ylim(-vista_max, vista_max)\cb1 \
\cb3 ax.set_aspect(\cf6 \strokec6 'equal'\cf0 \strokec4 )\cb1 \
\cb3 ax.grid(\cf7 \strokec7 True\cf0 \strokec4 )\cb1 \
\cb3 ax.set_title(\cf6 \strokec6 "Trayectoria Orbital 2D"\cf0 \strokec4 )\cb1 \
\cb3 ax.set_xlabel(\cf6 \strokec6 "X (km)"\cf0 \strokec4 )\cb1 \
\cb3 ax.set_ylabel(\cf6 \strokec6 "Y (km)"\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf0 \strokec4  usar_gradiente_color \cf7 \strokec7 and\cf0 \strokec4  \cf10 \strokec10 len\cf0 \strokec4 (vel_list) > \cf8 \strokec8 1\cf0 \strokec4  \cf7 \strokec7 and\cf0 \strokec4  \cf10 \strokec10 len\cf0 \strokec4 (vel_list) == \cf10 \strokec10 len\cf0 \strokec4 (x_km) - \cf8 \strokec8 1\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     velocities = np.array(vel_list)\cb1 \
\cb3     points = np.array([x_km, y_km]).T.reshape(\cf8 \strokec8 -1\cf0 \strokec4 , \cf8 \strokec8 1\cf0 \strokec4 , \cf8 \strokec8 2\cf0 \strokec4 )\cb1 \
\cb3     segments = np.concatenate([points[:\cf8 \strokec8 -1\cf0 \strokec4 ], points[\cf8 \strokec8 1\cf0 \strokec4 :]], axis=\cf8 \strokec8 1\cf0 \strokec4 )\cb1 \
\cb3     norm = mcolors.Normalize(vmin=velocities.\cf10 \strokec10 min\cf0 \strokec4 (), vmax=velocities.\cf10 \strokec10 max\cf0 \strokec4 ())\cb1 \
\cb3     lc = LineCollection(segments, cmap=\cf6 \strokec6 'plasma'\cf0 \strokec4 , norm=norm)\cb1 \
\cb3     lc.set_array(velocities)\cb1 \
\cb3     lc.set_linewidth(\cf8 \strokec8 2\cf0 \strokec4 )\cb1 \
\cb3     ax.add_collection(lc)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 else\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     ax.plot(x_km, y_km, \cf6 \strokec6 'b-'\cf0 \strokec4 , label=\cf6 \strokec6 'Trayectoria'\cf0 \strokec4 )\cb1 \
\
\cb3 ax.plot(x_km[\cf8 \strokec8 -1\cf0 \strokec4 ], y_km[\cf8 \strokec8 -1\cf0 \strokec4 ], \cf6 \strokec6 'ro'\cf0 \strokec4 , label=\cf6 \strokec6 'Sat\'e9lite'\cf0 \strokec4 )\cb1 \
\cb3 ax.add_patch(Circle((\cf8 \strokec8 0\cf0 \strokec4 , \cf8 \strokec8 0\cf0 \strokec4 ), radius=radio_del_cuerpo, color=\cf6 \strokec6 'goldenrod'\cf0 \strokec4 , label=\cf6 \strokec6 'Cuerpo central'\cf0 \strokec4 ))\cb1 \
\cb3 ax.add_patch(Circle((x_km[\cf8 \strokec8 -1\cf0 \strokec4 ], y_km[\cf8 \strokec8 -1\cf0 \strokec4 ]), radius=radio_satelite, color=\cf6 \strokec6 'red'\cf0 \strokec4 , alpha=\cf8 \strokec8 0.5\cf0 \strokec4 , label=\cf6 \strokec6 'Sat\'e9lite f\'edsico'\cf0 \strokec4 ))\cb1 \
\cb3 ax.legend()\cb1 \
\cb3 plt.show()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # --- ANIMACI\'d3N ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf0 \strokec4  mostrar_animacion:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf5 \strokec5 from\cf0 \strokec4  matplotlib \cf5 \strokec5 import\cf0 \strokec4  animation, rc\cb1 \
\cb3     rc(\cf6 \strokec6 'animation'\cf0 \strokec4 , html=\cf6 \strokec6 'jshtml'\cf0 \strokec4 )\cb1 \
\cb3     fig2, ax2 = plt.subplots(figsize=(\cf8 \strokec8 8\cf0 \strokec4 ,\cf8 \strokec8 8\cf0 \strokec4 ))\cb1 \
\cb3     ax2.set_xlim(x_km.\cf10 \strokec10 min\cf0 \strokec4 () - margin_x, x_km.\cf10 \strokec10 max\cf0 \strokec4 () + margin_x)\cb1 \
\cb3     ax2.set_ylim(y_km.\cf10 \strokec10 min\cf0 \strokec4 () - margin_y, y_km.\cf10 \strokec10 max\cf0 \strokec4 () + margin_y)\cb1 \
\cb3     ax2.set_aspect(\cf6 \strokec6 'equal'\cf0 \strokec4 )\cb1 \
\cb3     ax2.grid(\cf7 \strokec7 True\cf0 \strokec4 )\cb1 \
\cb3     ax2.set_title(\cf6 \strokec6 "Simulaci\'f3n orbital animada"\cf0 \strokec4 )\cb1 \
\cb3     ax2.set_xlabel(\cf6 \strokec6 "X (km)"\cf0 \strokec4 )\cb1 \
\cb3     ax2.set_ylabel(\cf6 \strokec6 "Y (km)"\cf0 \strokec4 )\cb1 \
\
\cb3     \cf5 \strokec5 if\cf0 \strokec4  usar_gradiente_color \cf7 \strokec7 and\cf0 \strokec4  \cf10 \strokec10 len\cf0 \strokec4 (vel_list) == \cf10 \strokec10 len\cf0 \strokec4 (x_km) - \cf8 \strokec8 1\cf0 \strokec4 :\cb1 \
\cb3         norm = mcolors.Normalize(vmin=\cf10 \strokec10 min\cf0 \strokec4 (vel_list), vmax=\cf10 \strokec10 max\cf0 \strokec4 (vel_list))\cb1 \
\cb3         cmap = plt.get_cmap(\cf6 \strokec6 'plasma'\cf0 \strokec4 )\cb1 \
\cb3     linea, = ax2.plot([], [], \cf6 \strokec6 '-'\cf0 \strokec4 , lw=\cf8 \strokec8 2\cf0 \strokec4 )\cb1 \
\cb3     sat_patch = Circle((x_km[\cf8 \strokec8 0\cf0 \strokec4 ], y_km[\cf8 \strokec8 0\cf0 \strokec4 ]), radius=radio_satelite, color=\cf6 \strokec6 'red'\cf0 \strokec4 , alpha=\cf8 \strokec8 0.5\cf0 \strokec4 )\cb1 \
\cb3     ax2.add_patch(sat_patch)\cb1 \
\cb3     punto, = ax2.plot([], [], \cf6 \strokec6 'ro'\cf0 \strokec4 , markersize=\cf8 \strokec8 5\cf0 \strokec4 )\cb1 \
\cb3     estrella = Circle((\cf8 \strokec8 0\cf0 \strokec4 , \cf8 \strokec8 0\cf0 \strokec4 ), radius=radio_del_cuerpo, color=\cf6 \strokec6 'goldenrod'\cf0 \strokec4 , label=\cf6 \strokec6 'Cuerpo central'\cf0 \strokec4 )\cb1 \
\cb3     ax2.add_patch(estrella)\cb1 \
\
\cb3     \cf7 \strokec7 def\cf0 \strokec4  \cf10 \strokec10 init\cf0 \strokec4 ():\cb1 \
\cb3         linea.set_data([], [])\cb1 \
\cb3         punto.set_data([], [])\cb1 \
\cb3         sat_patch.center = (x_km[\cf8 \strokec8 0\cf0 \strokec4 ], y_km[\cf8 \strokec8 0\cf0 \strokec4 ])\cb1 \
\cb3         \cf5 \strokec5 return\cf0 \strokec4  linea, punto, estrella, sat_patch\cb1 \
\
\cb3     \cf7 \strokec7 def\cf0 \strokec4  \cf10 \strokec10 update\cf0 \strokec4 (\cf11 \strokec11 frame\cf0 \strokec4 ):\cb1 \
\cb3         i = frame * salto_de_frames\cb1 \
\cb3         \cf5 \strokec5 if\cf0 \strokec4  i < \cf8 \strokec8 2\cf0 \strokec4 :\cb1 \
\cb3             \cf5 \strokec5 return\cf0 \strokec4  linea, punto, estrella, sat_patch\cb1 \
\cb3         i = \cf10 \strokec10 min\cf0 \strokec4 (i, \cf10 \strokec10 len\cf0 \strokec4 (x_km) - \cf8 \strokec8 1\cf0 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 if\cf0 \strokec4  usar_gradiente_color \cf7 \strokec7 and\cf0 \strokec4  \cf10 \strokec10 len\cf0 \strokec4 (vel_list) == \cf10 \strokec10 len\cf0 \strokec4 (x_km) - \cf8 \strokec8 1\cf0 \strokec4 :\cb1 \
\cb3             color = cmap(norm(vel_list[i]))\cb1 \
\cb3             linea.set_color(color)\cb1 \
\cb3         linea.set_data(x_km[:i+\cf8 \strokec8 1\cf0 \strokec4 ], y_km[:i+\cf8 \strokec8 1\cf0 \strokec4 ])\cb1 \
\cb3         punto.set_data([x_km[i]], [y_km[i]])\cb1 \
\cb3         sat_patch.center = (x_km[i], y_km[i])\cb1 \
\cb3         \cf5 \strokec5 return\cf0 \strokec4  linea, punto, estrella, sat_patch\cb1 \
\
\cb3     frames_total = \cf10 \strokec10 len\cf0 \strokec4 (x_km) // salto_de_frames\cb1 \
\cb3     anim = animation.FuncAnimation(fig2, update, init_func=init, frames=frames_total, interval=velocidad_animacion, blit=\cf7 \strokec7 True\cf0 \strokec4 )\cb1 \
\
\cb3     \cf5 \strokec5 if\cf0 \strokec4  formato_exportacion == \cf6 \strokec6 "GIF"\cf0 \strokec4 :\cb1 \
\cb3         anim.save(\cf6 \strokec6 "orbita.gif"\cf0 \strokec4 , writer=\cf6 \strokec6 "pillow"\cf0 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 elif\cf0 \strokec4  formato_exportacion == \cf6 \strokec6 "MP4"\cf0 \strokec4 :\cb1 \
\cb3         anim.save(\cf6 \strokec6 "orbita.mp4"\cf0 \strokec4 , writer=\cf6 \strokec6 "ffmpeg"\cf0 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 else\cf0 \strokec4 :\cb1 \
\cb3         display(HTML(anim.to_jshtml()))\cb1 \
\cb3     plt.close(fig2)\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 #-------------------------------------------------A----------------------------------A-------------------------------------\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #------------------------------------------------AAA--------------------------------AAA--------------------------------------\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #-------------------------------------------------A----------------------------------A-------------------------------------\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf0 \strokec4  \cf10 \strokec10 len\cf0 \strokec4 (x_km) == \cf8 \strokec8 1\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 # Repetimos un segundo punto para que el gr\'e1fico tenga escala\cf0 \cb1 \strokec4 \
\cb3     x_km = np.append(x_km, x_km[\cf8 \strokec8 0\cf0 \strokec4 ] + \cf8 \strokec8 1\cf0 \strokec4 )\cb1 \
\cb3     y_km = np.append(y_km, y_km[\cf8 \strokec8 0\cf0 \strokec4 ] + \cf8 \strokec8 1\cf0 \strokec4 )\cb1 \
\
\cb3 ax.plot(x_km[\cf8 \strokec8 -1\cf0 \strokec4 ], y_km[\cf8 \strokec8 -1\cf0 \strokec4 ], \cf6 \strokec6 'ro'\cf0 \strokec4 , label=\cf6 \strokec6 'Sat\'e9lite'\cf0 \strokec4 )\cb1 \
\cb3 ax.add_patch(Circle((\cf8 \strokec8 0\cf0 \strokec4 , \cf8 \strokec8 0\cf0 \strokec4 ), radius=radio_del_cuerpo, color=\cf6 \strokec6 'goldenrod'\cf0 \strokec4 , label=\cf6 \strokec6 'Cuerpo central'\cf0 \strokec4 ))\cb1 \
\cb3 ax.add_patch(Circle((x_km[\cf8 \strokec8 -1\cf0 \strokec4 ], y_km[\cf8 \strokec8 -1\cf0 \strokec4 ]), radius=radio_satelite*\cf8 \strokec8 0.01\cf0 \strokec4 , color=\cf6 \strokec6 'gray'\cf0 \strokec4 , alpha=\cf8 \strokec8 0.5\cf0 \strokec4 ))\cb1 \
\cb3 ax.legend()\cb1 \
\cb3 plt.show()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf0 \strokec4  colision:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf10 \strokec10 print\cf0 \strokec4 (\cf7 \strokec7 f\cf6 \strokec6 "\uc0\u9201 \u65039  Tiempo hasta colisi\'f3n: \cf0 \strokec4 \{\cf10 \strokec10 len\cf0 \strokec4 (x_list)*dt\cf8 \strokec8 :.2f\cf0 \strokec4 \}\cf6 \strokec6  s"\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf0 \strokec4  colision:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf10 \strokec10 print\cf0 \strokec4 (\cf7 \strokec7 f\cf6 \strokec6 "\uc0\u9732 \u65039  El sat\'e9lite colision\'f3 con el cuerpo central tras \cf0 \strokec4 \{\cf10 \strokec10 len\cf0 \strokec4 (x_list) * dt\cf8 \strokec8 :.2f\cf0 \strokec4 \}\cf6 \strokec6  s."\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 else\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     r0 = np.sqrt(x_list[\cf8 \strokec8 0\cf0 \strokec4 ]**\cf8 \strokec8 2\cf0 \strokec4  + y_list[\cf8 \strokec8 0\cf0 \strokec4 ]**\cf8 \strokec8 2\cf0 \strokec4 )\cb1 \
\cb3     E = \cf8 \strokec8 0.5\cf0 \strokec4  * (vx**\cf8 \strokec8 2\cf0 \strokec4  + vy**\cf8 \strokec8 2\cf0 \strokec4 ) - G * masa_central / r0\cb1 \
\cb3     \cf10 \strokec10 print\cf0 \strokec4 (\cf6 \strokec6 "\uc0\u55356 \u57088  \'d3rbita estable."\cf0 \strokec4  \cf5 \strokec5 if\cf0 \strokec4  E < \cf8 \strokec8 0\cf0 \strokec4  \cf5 \strokec5 else\cf0 \strokec4  \cf6 \strokec6 "\uc0\u55357 \u56960  Escape."\cf0 \strokec4  \cf5 \strokec5 if\cf0 \strokec4  E > \cf8 \strokec8 0\cf0 \strokec4  \cf5 \strokec5 else\cf0 \strokec4  \cf6 \strokec6 "\uc0\u55357 \u57313  \'d3rbita parab\'f3lica."\cf0 \strokec4 , \cf7 \strokec7 f\cf6 \strokec6 "Energ\'eda total = \cf0 \strokec4 \{E\cf8 \strokec8 :.2e\cf0 \strokec4 \}\cf6 \strokec6  J"\cf0 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 if\cf0 \strokec4  \cf10 \strokec10 len\cf0 \strokec4 (dist_list) > \cf8 \strokec8 1\cf0 \strokec4 :\cb1 \
\cb3         r_min = np.\cf10 \strokec10 min\cf0 \strokec4 (dist_list)\cb1 \
\cb3         r_max = np.\cf10 \strokec10 max\cf0 \strokec4 (dist_list)\cb1 \
\cb3         a = \cf8 \strokec8 0.5\cf0 \strokec4  * (r_max + r_min)\cb1 \
\cb3         periodo = \cf8 \strokec8 2\cf0 \strokec4  * np.pi * np.sqrt(a**\cf8 \strokec8 3\cf0 \strokec4  / (G * masa_central))\cb1 \
\cb3         excentricidad = (r_max - r_min) / (r_max + r_min)\cb1 \
\cb3         \cf10 \strokec10 print\cf0 \strokec4 (\cf7 \strokec7 f\cf6 \strokec6 "\uc0\u55357 \u56527  Distancia m\'ednima: \cf0 \strokec4 \{r_min/\cf8 \strokec8 1_000:.2f\cf0 \strokec4 \}\cf6 \strokec6  km"\cf0 \strokec4 )\cb1 \
\cb3         \cf10 \strokec10 print\cf0 \strokec4 (\cf7 \strokec7 f\cf6 \strokec6 "\uc0\u55357 \u56528  Distancia m\'e1xima: \cf0 \strokec4 \{r_max/\cf8 \strokec8 1_000:.2f\cf0 \strokec4 \}\cf6 \strokec6  km"\cf0 \strokec4 )\cb1 \
\cb3         \cf10 \strokec10 print\cf0 \strokec4 (\cf7 \strokec7 f\cf6 \strokec6 "\uc0\u55357 \u56480  Excentricidad: \cf0 \strokec4 \{excentricidad\cf8 \strokec8 :.3f\cf0 \strokec4 \}\cf6 \strokec6 "\cf0 \strokec4 )\cb1 \
\cb3         \cf10 \strokec10 print\cf0 \strokec4 (\cf7 \strokec7 f\cf6 \strokec6 "\uc0\u55357 \u56658  Per\'edodo estimado: \cf0 \strokec4 \{periodo\cf8 \strokec8 :.2f\cf0 \strokec4 \}\cf6 \strokec6  s"\cf0 \strokec4 )\cb1 \
\
}