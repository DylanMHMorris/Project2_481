from logic import *

# Dylan Morris, Michael Morikawa, Kevin La, Dylan Tran

ATruthoraptor = Symbol("A is a Truthoraptor")
ALieosaurus = Symbol("A is a Lieosaurus")

BTruthoraptor = Symbol("B is a Truthoraptor")
BLieosaurus = Symbol("B is a Lieosaurus")

CTruthoraptor = Symbol("C is a Truthoraptor")
CLieosaurus = Symbol("C is a Lieosaurus")


# The puzzle states that a dinosaur can't be both
# So use this logic as a base for each puzzle
UNIVERSAL_LOGIC = And(
    Or(ATruthoraptor, ALieosaurus),
    Not(And(ATruthoraptor, ALieosaurus)),
    Or(BTruthoraptor, BLieosaurus),
    Not(And(BTruthoraptor, BLieosaurus)),
    Or(CTruthoraptor, CLieosaurus)
)

# Puzzle 0
# A says "I am both a Truthoraptor and a Lieosaurus."

AStatement0 = And(ATruthoraptor, ALieosaurus)
knowledge0 = And(
    UNIVERSAL_LOGIC,
    Implication(ATruthoraptor, AStatement0),
    Implication(ALieosaurus, Not(AStatement0)),
)

# Puzzle 1
# A says "We are both Lieosauruss."
# B says nothing.
AStatement1 = And(ALieosaurus, BLieosaurus)
knowledge1 = And(
    UNIVERSAL_LOGIC,
    Implication(ATruthoraptor, AStatement1),
    Implication(ALieosaurus, Not(AStatement1)),
)


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
AStatement2 = Or(And(ATruthoraptor, BTruthoraptor), And(ALieosaurus, BLieosaurus))
BStatement2 = Or(And(ATruthoraptor, BLieosaurus), And(ALieosaurus, BTruthoraptor))

knowledge2 = And(
    UNIVERSAL_LOGIC,
    Implication(ATruthoraptor, AStatement2),
    Implication(ALieosaurus, Not(AStatement2)),
    Implication(BTruthoraptor, Or(BStatement2)),
    Implication(BLieosaurus, Not(BStatement2)))

# Puzzle 3
# A says either "I am a Truthoraptor." or "I am a Lieosaurus.", but you don't know which.
# B says "A said 'I am a Lieosaurus'."
# B says "C is a Lieosaurus."
# C says "A is a Truthoraptor."
AStatement3 = Or(ATruthoraptor, ALieosaurus)
BStatement3 = CLieosaurus
CStatement3 = ATruthoraptor

knowledge3 = And(
    UNIVERSAL_LOGIC,
    Not(And(CTruthoraptor, CLieosaurus)),
    Implication(ATruthoraptor, AStatement3),
    Implication(ALieosaurus, Not(AStatement3)),
    Implication(BTruthoraptor, BStatement3),
    Implication(BLieosaurus, Not(BStatement3)),
    Implication(CTruthoraptor, CStatement3),
    Implication(CLieosaurus, Not(CStatement3)),
)


def main():
    symbols = [
        ATruthoraptor,
        ALieosaurus,
        BTruthoraptor,
        BLieosaurus,
        CTruthoraptor,
        CLieosaurus,
    ]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
