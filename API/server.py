import os
from waitress import serve
# Cambia 'app' por el nombre de tu archivo principal si es distinto (ej. from main import app)
from api import app 

if __name__ == '__main__':
    # IIS inyecta el puerto dinámico en esta variable de entorno. 
    # Si no la encuentra (uso local), usa el 5000.
    port = int(os.environ.get('HTTP_PLATFORM_PORT', 5000))
    
    print(f"Iniciando servidor Waitress en el puerto {port}...")
    serve(app, host='127.0.0.1', port=port)
