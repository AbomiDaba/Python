import ninja
import pet

ninja = ninja.Ninja("Bob", "Johnson", "bone", "scooby snacks", pet.Pet("scooby doo", "dog", "talk"))

ninja.feed().walk().bathe()
