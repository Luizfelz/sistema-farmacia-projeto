import os

def limpar_prompt():
    # windows
    if os.name == 'nt':
      _ = os.system('cls')

    # mac / linux
    else:
      _ = os.system('clear')