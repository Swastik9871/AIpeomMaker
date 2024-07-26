import random

# Lists of words and phrases to use in the poem
nouns = ["love", "heart", "hate", "moon", "tree", "river", "sky", "mountain", "ocean", "star"]
verbs = ["runs", "flies", "sings", "whispers", "shines", "dreams", "cries"]
adjectives = ["blue", "bright", "happy", "sad", "dark", "mysterious", "silent", "noisy", "colorful", "peaceful"]
prepositions = ["in the", "under the", "over the", "beside the", "with the"]
emojis = ["🌸", "️🤍", "🕊️", "🌕", "💖", "🍂", "🌌", "🎼", "✨", "🌟"]

def article(word):
    return "an" if word[0].lower() in 'aeiou' else "a"

def generate_line():
    structure = random.choice([1, 2, 3])
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    preposition = random.choice(prepositions)
    emoji = random.choice(emojis)
::    
    if structure == 1:
        return f"The {adjective} {noun} {verb} {preposition} {random.choice(nouns)} {emoji}"
    elif structure == 2:
        return f"{article(adjective)} {adjective} {noun} {verb} {preposition} {random.choice(nouns)} {emoji}"
    else:
        return f"{article(noun)} {noun} {verb} {preposition} {random.choice(adjectives)} {random.choice(nouns)} {emoji}"

def generate_poem(lines=4):
    poem = [generate_line() for _ in range(lines)]
    return "\n".join(poem)


print(generate_poem())