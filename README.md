# Sentiment_Analysis
Short text sentiment detection

How to use:

```
from sentiment import detect
detect(string)
```

Examples:
1. Negative example
```
detect('Ты мне не нравишься')

>> {'string': 'Ты мне не нравишься', 'sentiment': 'negative'}
```
2. Positive example
```
detect('Выглядишь просто чудесно')

>> {'string': 'Выглядишь просто чудесно', 'sentiment': 'positive'}
```
3. Neutral example
```
detect('Позови мне этого человека')

>> {'string': 'Позови мне этого человека', 'sentiment': 'neutral'}
```
