# Generating Randomness

This is a Python-based game that uses a simple form of AI to predict user input. The game is based on the concept of triads, which are sequences of three consecutive characters. The AI learns from the user's input and makes predictions based on the frequency of triads.

## How to Play

1. The game starts by asking the user to input a string of at least 100 characters, consisting of '0's and '1's. This is used to train the AI.

2. The user is then asked to input a string of at least 4 characters. The AI will predict the next character based on the triads in the user's input.

3. The AI's prediction is compared with the actual next character. If the prediction is correct, the user loses $1 from their balance. If the prediction is incorrect, the user gains $1.

4. The game continues until the user decides to stop or their balance reaches 0.

## Installation

This game requires Python 3.9 or later. You can install it by cloning the repository and running the `predictor.py` file.

```bash
git clone https://github.com/davidrmellors/GeneratingRandomness.git
cd GeneratingRandomness
python predictor.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
