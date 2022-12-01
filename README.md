# Pokemon Battle :: Unitechies 23-1

- Para comenzar un juego, tú como jugador debes elegir un nombre y un tipo de personaje.

- Según el tipo seleccionado, tendrás un conjunto de puntos y movimientos para desafiar al Bot generado por el software.

- Una vez que ingreses a la batalla, deberás elegir un movimiento para desafiar al Bot, si las cosas van bien, lo dañarás, de lo contrario, serás dañado.

- La batalla continuará hasta que uno de ustedes se desmaye.

- Si ese es el caso, el juego declarará un ganador.

## Diagrama de secuencia

Esta es la secuencia que deberá seguir el software a desarrollar.

![Diagrama de secuencia](diagrams/activities.jpeg)

## Diagrama de clases

Estas son las clases sugeridas para completar el software, el software puede variar si el equipo lo considera adecuado siempre y cuando el resultado final sea el mismo.

![Diagrama de clases](diagrams/classes.jpeg)

## Script de ejecución (`main.py`)

```python
game = Game()

game.ask_username() # Cómo te llamas?
game.show_characters() # bulbasaur, charmander, squirtle, pikachu, snorlax, pidgeotto
game.ask_character() # Qué personaje quieres utilizar?
game.setup_player() # Inicializa el jugador
game.setup_bot() # Inicializa el bot
game.setup_battle() #  "{player.name} reta al {bot.character.name} de {bot.name} con {@player.character.name}"
game.run_battle()
```
