# NYT Spelling Bee Hints

This app is to provide hints for NYT spelling bee.

### How this works

1. You have to specify the center letter and other letters from [NYT spelling bee](https://www.nytimes.com/puzzles/spelling-bee).
2. It uses a comprehensive word list from this [github repo](https://github.com/dwyl/english-words) to check for candidate words. This repo while extensive contains several invalid words. So,
3. It checks the MerriamWebster Dictionary API to check for valid words and their meanings
4. When you click on give hint, it generates part of a word, its meaning and length

### To deploy it on your own

1. Download the repo
2. Create a .streamlit/secrets.toml file, and set DICTIONARY_API_KEY as the API key from dictionaryapi.com.

### Packages you will need

```
pip install -r requirements.txt
```

### To run the app

```
streamlit run spelling_bee_hints.py
```
