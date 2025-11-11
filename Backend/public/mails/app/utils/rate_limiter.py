"""
===============================================================================
Archivo:        rate_limiter.py
Ubicación:      app/utils/rate_limiter.py
Descripción:    Implementa un limitador de tasa (Rate Limiter) en memoria para
                controlar la frecuencia de solicitudes de los usuarios. 
                Evita abusos y sobrecargas limitando la cantidad de acciones 
                permitidas en una ventana de tiempo configurable.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/11/10
Radicado:       v0010af
===============================================================================
"""

from time import time


class RateLimiter:
    """
    Implementa un limitador de tasa simple basado en memoria.

    Utiliza un diccionario en memoria para registrar los timestamps de las
    solicitudes de cada usuario y determinar si se permite o bloquea una nueva
    acción, según la cantidad de llamadas en la ventana temporal definida.

    Atributos
    ---------
    max_calls : int
        Número máximo de llamadas permitidas por usuario dentro de la ventana.
    window_seconds : int
        Duración de la ventana de tiempo (en segundos) para medir las llamadas.
    calls : dict[str, list[float]]
        Registro de timestamps (en segundos) de las solicitudes por usuario.
    """

    def __init__(self, max_calls: int = 10, window_seconds: int = 3600):
        """
        Inicializa el rate limiter con los parámetros definidos.

        Parámetros
        ----------
        max_calls : int, opcional
            Número máximo de llamadas permitidas por usuario. (por defecto: 10)
        window_seconds : int, opcional
            Duración de la ventana de control en segundos. (por defecto: 3600 = 1 hora)
        """
        self.max_calls = max_calls
        self.window_seconds = window_seconds
        self.calls = {}

    # -------------------------------------------------------------------------
    # MÉTODO PRINCIPAL
    # -------------------------------------------------------------------------
    def is_allowed(self, user_id: str) -> bool:
        """
        Determina si un usuario puede realizar una nueva solicitud.

        Parámetros
        ----------
        user_id : str
            Identificador único del usuario (por ejemplo, `sub` del JWT).

        Retorna
        -------
        bool
            `True` si el usuario puede realizar la acción.
            `False` si alcanzó el límite permitido en la ventana de tiempo.

        Ejemplo
        -------
        >>> limiter = RateLimiter(max_calls=3, window_seconds=60)
        >>> for i in range(5):
        ...     print(limiter.is_allowed("user123"))
        True
        True
        True
        False
        False
        """
        now = time()
        user_calls = self.calls.get(user_id, [])

        # Filtrar solo las llamadas dentro de la ventana válida
        user_calls = [c for c in user_calls if now - c < self.window_seconds]

        # Si supera el límite de llamadas, bloquear
        if len(user_calls) >= self.max_calls:
            return False

        # Registrar la nueva llamada
        user_calls.append(now)
        self.calls[user_id] = user_calls
        return True


# -------------------------------------------------------------------------------
# Instancia global del limitador de tasa
# -------------------------------------------------------------------------------
rate_limiter = RateLimiter()
