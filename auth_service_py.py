from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

# Crea una instancia de la aplicación FastAPI
app = FastAPI()

# Clave secreta y algoritmo para la generación y decodificación de tokens JWT
SECRET_KEY = "12345"
ALGORITHM = "HS256"

# Configuración del esquema de OAuth2 para el manejo de tokens de contraseña
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Función de prueba para verificar que el servicio de autenticación está en funcionamiento
def auth_app():
    return {"message": "Authentication service is up and running"}

# Función para obtener el usuario actual a partir del token JWT
def get_current_user(token: str = Depends(oauth2_scheme)):
    # Excepción a lanzar en caso de problemas de autenticación
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decodifica el token utilizando la clave secreta y el algoritmo definido
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Obtiene el nombre de usuario (sub) del payload del token
        username: str = payload.get("sub")
        # Si no hay nombre de usuario, lanza una excepción
        if username is None:
            raise credentials_exception
    except JWTError:
        # Si hay un error en la decodificación del token, lanza una excepción
        raise credentials_exception
    # Retorna el nombre de usuario
    return username

# Ruta para el endpoint de login
@app.post("/token", response_model=dict)
async def login(form_data: dict = Depends(oauth2_scheme)):
    # Verifica las credenciales proporcionadas en el formulario
    if form_data.get("username") == "user" and form_data.get("password") == "password":
        # Genera un token JWT si las credenciales son válidas
        token = jwt.encode({"sub": form_data["username"]}, SECRET_KEY, algorithm=ALGORITHM)
        # Retorna el token generado junto con el tipo de token
        return {"access_token": token, "token_type": "bearer"}
    else:
        # Si las credenciales no son válidas, lanza una excepción
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
