# Base de datos

## Diagrama de base de datos

![Diagrama de base de datos](/BaseDeDatos/DiagramaDeBaseDeDatos.png)

## Base de datos en Mongo DB

Elección de MongoDB para el Sistema de Detección de Armas
📌 ¿Por qué MongoDB?
MongoDB es la base de datos ideal para este proyecto debido a su esquema flexible, alto rendimiento en tiempo real y escalabilidad, características clave para un sistema de visión por computadora que procesa flujos de video continuos.

✅ Ventajas Clave
1. 🔄 Esquema Flexible (NoSQL)
Adaptabilidad: Permite guardar datos variables como coordenadas de detección (bounding_box), confianza del modelo y metadatos de imágenes sin restricciones de esquema rígido.

Fácil evolución: Si el modelo YOLOv11 mejora o se añaden nuevos tipos de armas, no se requieren migraciones complejas.

2. ⚡ Alto Rendimiento en Tiempo Real
Inserción rápida: Optimizado para manejar 15+ FPS (requerimiento del proyecto) con múltiples detecciones por frame.

Índices eficientes: Consultas rápidas para filtrar detecciones por tipo de arma, fecha o nivel de confianza.

3. 📈 Escalabilidad Horizontal
Sharding nativo: Distribuye la carga si el sistema crece (ej: más cámaras en red).

Crecimiento sin límites: Soporta terabytes de datos de imágenes y registros de detección.

4. 🖼️ Manejo de Datos Multimodales
Almacenamiento de metadatos: Guarda rutas de imágenes, miniaturas (Base64) y atributos de detección en un mismo documento.

Subdocumentos anidados: Ejemplo:

{
  "detected_at": "2024-05-20T14:30:00Z",
  "weapon_type": "pistola",
  "bounding_box": {"x": 100, "y": 150, "width": 80, "height": 60},
  "image_metadata": {"ruta": "/detections/img123.jpg", "resolución": "1920x1080"}
}
5. 🤖 Integración con Python y YOLOv11
PyMongo: Librería oficial para conectar el script de detección con MongoDB.

Agregaciones en tiempo real: Consultas como:

## "Obtener todas las pistolas detectadas con >85% de confianza en la última hora"
pipeline = [
    {"$match": {"weapon_type": "pistola", "confidence": {"$gt": 0.85}, "detected_at": {"$gte": hora_anterior}}},
    {"$count": "total_detecciones"}
]
6. 🗑️ Limpieza Automática (TTL Index)
Auto-borrado de datos antiguos: Ejemplo para eliminar detecciones de hace 30 días:

db.detections.createIndex({"detected_at": 1}, {expireAfterSeconds: 2592000})
🔍 Comparación con Bases de Datos SQL
Requisito	MongoDB	SQL (MySQL/PostgreSQL)
Estructura de datos	Documentos flexibles (JSON)	Tablas rígidas con esquema fijo
Rendimiento en inserciones	Óptimo para flujos continuos	Requiere optimización para alta velocidad
Escalabilidad	Horizontal (sharding automático)	Vertical (hardware más potente)
Consulta de datos anidados	Nativo (ej: detection.bounding_box.x)	Requiere JOINs o columnas JSON

🚀 Conclusión
MongoDB es la mejor opción para este proyecto porque:

Alinea con la naturaleza del sistema: Datos semi-estructurados, alta velocidad de escritura y necesidad de escalabilidad.

Soporta los requisitos no funcionales: 15+ FPS, alertas en tiempo real y bajo latency.

Facilita mantenimiento y crecimiento: Sin esquemas fijos y con herramientas nativas para análisis de datos.

💡 Nota: Si en el futuro se requieren análisis históricos complejos (ej: machine learning con datos antiguos), se puede complementar con un data warehouse como PostgreSQL + TimescaleDB, pero MongoDB sigue siendo ideal para la capa operacional.

📂 Estructura de la Base de Datos

📂 weapon_detection_db  
├── 📄 detections          # Registros de armas detectadas  
├── 📄 weapon_types        # Tipos de armas (pistola, rifle, etc.)  
├── 📄 images              # Metadatos de imágenes/frames procesados  
└── 📄 system_metrics      # Rendimiento del sistema (FPS, uso de CPU/GPU)  

Puedes encontrar el script completo de creación en BaseDeDatos/scriptMongoDB.

[Ver script](https://github.com/Dgomez-cpp/DetectorDeArmas/blob/main/BaseDeDatos/scriptMongoDB.txt)
