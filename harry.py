from logic import *

rain = Symbol("rain")
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")
snape = Symbol("snape")

knowledge = And(
    Implication(Not(rain), hagrid),

    Or(hagrid, dumbledore, snape),

    Not(And(hagrid, dumbledore)),
    Not(And(hagrid, snape)),
    Not(And(dumbledore, snape)),

    Implication(rain, Not(snape)),

    dumbledore,
    snape
)

print("rain:", model_check(knowledge, rain))
print("hagrid:", model_check(knowledge, hagrid))
print("dumbledore:", model_check(knowledge, dumbledore))
print("snape:", model_check(knowledge, snape))
