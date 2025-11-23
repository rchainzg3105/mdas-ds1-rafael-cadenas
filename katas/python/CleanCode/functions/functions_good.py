# Cumplimiento de Clean Code: Funciones Bien Diseñadas
# ✅ Solución: Una cosa por función, pequeñas, mismo nivel de abstracción, sin efectos secundarios

from typing import Dict, TypedDict


class User(TypedDict):
    name: str
    score: int


class UserScoreProcessor:
    FAST_TIME_BONUS = 10
    FAST_TIME_THRESHOLD_SECONDS = 60

    # ✅ Función hace UNA cosa: orquestar el procesamiento del puntaje
    # ✅ Mismo nivel de abstracción
    def process_user_score(self, user: User, new_score: int, time_in_seconds: int) -> None:
        bonus = self._calculate_bonus(time_in_seconds)
        final_score = user["score"] + new_score + bonus

        self._update_score(user, final_score)
        self._send_notification(user)
        self._log_activity(user, new_score)

    # ✅ Función pequeña que hace UNA cosa: calcular bonus
    def _calculate_bonus(self, time_in_seconds: int) -> int:
        if time_in_seconds < self.FAST_TIME_THRESHOLD_SECONDS:
            print(
                f"Aplica bonus de {self.FAST_TIME_BONUS} puntos por tiempo rápido.")
            return self.FAST_TIME_BONUS
        return 0

    # ✅ Función pequeña que hace UNA cosa: actualizar puntaje
    def _update_score(self, user: User, final_score: int) -> None:
        user["score"] = final_score

    # ✅ Función pequeña que hace UNA cosa: enviar notificación
    def _send_notification(self, user: User) -> None:
        print(
            f"Notificación enviada a {user['name']}: Tu nuevo puntaje es {user['score']}")

    # ✅ Función pequeña que hace UNA cosa: registrar actividad
    def _log_activity(self, user: User, new_score: int) -> None:
        print(
            f"LOG: {user['name']} obtuvo {new_score} puntos. Puntaje final: {user['score']}")


if __name__ == "__main__":
    # Uso
    print("=== Cumplimiento de Funciones en Clean Code ===")
    user: User = {"name": "Alex", "score": 100}
    processor = UserScoreProcessor()
    processor.process_user_score(user, 50, 30)
    print(f"Puntaje final del usuario: {user['score']}")

    # ✅ Si necesito cambiar _calculate_bonus() o _send_notification(), cambio una sola vez
    # ✅ Nuevas funcionalidades se agregan fácilmente
    # ✅ Consistencia garantizada
