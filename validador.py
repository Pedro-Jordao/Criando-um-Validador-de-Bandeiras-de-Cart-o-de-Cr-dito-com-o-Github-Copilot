import re

def luhn_check(card_number):
    digits = [int(d) for d in str(card_number)]
    checksum = 0
    parity = len(digits) % 2
    for i, digit in enumerate(digits):
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return checksum % 10 == 0

def detect_flag(card_number):
    num = str(card_number).replace(' ', '').replace('-', '')

    rules = [
        # MasterCard
        (r'^(5[1-5][0-9]{14}|222[1-9][0-9]{12}|22[3-9][0-9]{13}|2[3-6][0-9]{14}|27[01][0-9]{13}|2720[0-9]{12})$', 'MasterCard', [16]),
        # Visa
        (r'^4[0-9]{12}(?:[0-9]{3})?(?:[0-9]{3})?$', 'Visa', [13, 16, 19]),
        # American Express
        (r'^3[47][0-9]{13}$', 'American Express', [15]),
        # Diners Club (mantido conforme instruído)
        (r'^(3(0[0-5]|6|8|9|880)[0-9]{11})$', 'Diners Club', [14]),
        # Discover
        (r'^(6011[0-9]{12}|65[0-9]{14}|64[4-9][0-9]{13}|622(12[6-9]|1[3-9][0-9]|[2-8][0-9]{2}|9[01][0-9]|92[0-5])[0-9]{10})$', 'Discover', [16, 19]),
        # EnRoute
        (r'^(2014|2149)[0-9]{11}$', 'EnRoute', [15]),
        # JCB
        (r'^(35(2[89]|[3-8][0-9])[0-9]{12,15})$', 'JCB', [16, 17, 18, 19]),
        # Voyager
        (r'^8699[0-9]{11}$', 'Voyager', [15]),
        # Hipercard
        (r'^606282[0-9]{10}$', 'Hipercard', [16]),
        # Aura (corrigido)
        (r'^(5029|5040|5054|5059|5067|5081)[0-9]{12,15}$', 'Aura', [16, 17, 18, 19]),
    ]

    for pattern, flag, lengths in rules:
        if re.match(pattern, num) and len(num) in lengths:
            if luhn_check(num):
                return flag
            else:
                return f"{flag} (número inválido pelo Luhn)"
    return "Bandeira desconhecida ou número inválido"

# Exemplo de uso:
if __name__ == "__main__":
    test_cards = [
    # Visa
    "4835230978958033",
    "4076490381314721",
    "4715972907428058",
    # MasterCard
    "5519621027358996",
    "2221487573855905",
    "2221728611944031",
    # American Express
    "377869452565707",
    "374292287471241",
    "376319040569303",
    # Diners Club
    "36245727693866",
    "30558049833959",
    "36966076162750",
    # Discover
    "6011680481166215",
    "6534364449702164",
    "6011552899413802",
    # EnRoute
    "214926394412828",
    "214955194615741",
    "201403865704244",
    # JCB
    "3528801242377172",
    "3528690295337869",
    "3528902000383263",
    # Voyager
    "869993161078237",
    "869985866803732",
    "869953765070669",
    # Hipercard
    "6062821721956578",
    "6062826696562216",
    "6062822990374215",
    # Aura
    "5040685092023058",
    "5029745519245277",
    "5081587420848379",
    # Exemplo inválido
    "1234567890123456"
]

    for card in test_cards:
        print(f"{card}: {detect_flag(card)}")