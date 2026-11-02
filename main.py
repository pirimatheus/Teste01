import argparse


def main():
    parser = argparse.ArgumentParser(description="Descrição do seu script")
    parser.add_argument("--nome", help="Exemplo de argumento")
    args = parser.parse_args()
    print(f"Olá, {args.nome}")


if __name__ == "__main__":
    main()
