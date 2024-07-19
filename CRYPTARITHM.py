import itertools

def solve_cryptarithm(equation):
    words = equation.replace('=', '+').split('+')
    letters = set(''.join(words))
    
    if len(letters) > 10:
        return "Terlalu banyak huruf untuk dipetakan ke digit unik (maksimum 10 huruf)."
    
    for perm in itertools.permutations('0123456789', len(letters)):
        table = str.maketrans(''.join(letters), ''.join(perm))
        transformed_words = [word.translate(table) for word in words]
        
        if any(word[0] == '0' for word in transformed_words):
            continue
        
        if sum(map(int, transformed_words[:-1])) == int(transformed_words[-1]):
            return {letter: digit for letter, digit in zip(letters, perm)}
    
    return "Tidak ada solusi yang ditemukan."

# Contoh penggunaan
equation = input("Masukkan persamaan Cryptarithm (misalnya SEND + MORE = MONEY): ")
solution = solve_cryptarithm(equation)
print("Solusi:", solution)
