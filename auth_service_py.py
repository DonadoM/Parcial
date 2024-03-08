from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

app = FastAPI()

# Clave secreta para firmar y verificar tokens (reemplaza con tu clave real)
SECRET_KEY = "12345"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def auth_app():
    return {"message": "Authentication service is up and running"}


# Define la función get_current_user
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decodifica el token utilizando la clave secreta y el algoritmo especificado
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username


# Ruta para el endpoint de login
@app.post("/token", response_model=dict)
async def login(form_data: dict = Depends(oauth2_scheme)):
    # Lógica de autenticación (aquí, se asume un usuario y contraseña fijos)
    if form_data.get("username") == "user" and form_data.get("password") == "password":
        # Genera un token (simplificado para propósitos de ejemplo)
        token = jwt.encode({"sub": form_data["username"]}, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )