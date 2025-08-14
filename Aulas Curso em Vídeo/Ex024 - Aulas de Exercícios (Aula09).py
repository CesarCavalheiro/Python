cidade = input('Digite a cidade em que você nasceu: ').strip().title()
print(f"""Você nasceu em: {cidade}.
O nome da sua cidade começa com \"Santo\"? {cidade[:5].upper() == 'SANTO'}""")