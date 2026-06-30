from src.generation.generator import Generator


def main():

    model = Generator()
    answer = model.generate("Who developed BERT?")
    print(answer)


if __name__ == "__main__":
    print("*" * 50)
    main()
    print("x" * 50)