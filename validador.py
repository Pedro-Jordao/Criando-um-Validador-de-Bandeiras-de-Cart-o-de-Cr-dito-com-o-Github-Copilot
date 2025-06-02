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
        # Diners Club (corrigido)
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
        (r'^(5018|5020|5031|5041|5054|5066|5067|5093|5019)[0-9]{12,15}$', 'Aura', [16, 17, 18, 19]),
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
        "4111111111111111",  # Visa
        "5500000000000004",  # MasterCard
        "340000000000009",   # American Express
        "30000000000004",    # Diners Club
        "6011000000000004",  # Discover
        "201400000000009",   # EnRoute
        "3530111333300000",  # JCB
        "869900000000000",   # Voyager
        "6062825624254001",  # Hipercard
        "5093986995399521",  # Aura (exemplo que você trouxe)
        "30140431002441",    # Diners Club (exemplo que você trouxe)
        "1234567890123456",  # Inválido
    ]
    # for card in test_cards:
    #     print(f"{card}: {detect_flag(card)}")
print(detect_flag("5040 8305 7439 0739"))  # Teste específico para o exemplo que você trouxe