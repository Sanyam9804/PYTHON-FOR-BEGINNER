letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''

print(letter.replace("<|Name|>", "SANYAM"))
print(letter.replace("<|Date|>", "18/12/2024"))

### 2nd METHOD ##

print(letter.replace("<|Name|>", "SANYAM").replace("<|Date|>", "18/12/2024"))
