"""
Coding for AI - Problem Set 6
Lab Project: The DNA Sequence Marker Finder

Name: Tanishka Hira
Date: 09/09/2026

Call by Object Reference:
In Python, passing an argument to a function shares a
reference to the same underlying object rather than making
a copy or locking the variable itself. If you modify a
mutable object inside the function—like adding an item
to a list—that change directly impacts the original object
outside. However, if you reassign the variable name to an
entirely new object, it only updates that local binding,
leaving the original variable untouched.
"""

''' ---Task 1: Building search4letters--- '''
def search4letters(phrase: str, letters: str = 'ATCG') -> set:
    """Return the set of target 'letters' found in a supplied 'phrase'."""

    # set(letters) creates a unique pool of target markers    
    # set(phrase) represents the genetic material to analyze
    return set(letters).intersection(set(phrase))

print(" -- TASK 1 -- ")

''' 1. Positional arguments '''
result1 = search4letters('TGGACC', 'GC')
print("search4letters('TGGACC', 'GC'): ", result1)

''' 2. Keyword arguments '''
result2 = search4letters(letters='CG', phrase='TGGACC')
print("search4letters(letters='CG', phrase='TGGACC'):", result2)

''' 3. Default argument '''
result3 = search4letters('TGGACC')
print("search4letters('TGGACC'):", result3)



''' ---Task 2: Tracking Memory References--- '''
def analyze_sequence(sequence_list, marker):
    print(f"Inside Functions (Start) - ID: {id(sequence_list)} | Data: {sequence_list}")
    # In-place modification (mutating the shared object)
    sequence_list.append(marker)
    print(f"Inside Function (End)    - ID: {id(sequence_list)} | Data: {sequence_list}")

#Driver code
print(" -- TASK 2 -- ")
dna_database = ['AATCCG', 'TGGCTA']
print(f"Global Scope(Before)     - ID: {id(dna_database)} | Data: {dna_database}")
analyze_sequence(dna_database, 'CGAT')
print(f"Global Scope (After)     - ID: {id(dna_database)} | Data: {dna_database}")



'''3.2 The discovery challenge'''
print(" -- The Discovery challenge -- ")
print("Ques. Why was dna database modified in the global scope, even though analyze sequence never returned anything?")
print("Answer. Python’s argument-passing model is often described imprecisely as either “pass by reference” (the C++ sense) or “pass by value” (the sense used for primitives in Java or C) — neither term is accurate for Python. The precise description is call by object reference (sometimes called “call by sharing”): when you call analyze sequence(dna database, ’CGAT’), the parameter sequence list inside the function is bound to the exact same list object that dna database refers to in the global scope — not a copy of it, and not a reference-to-a-reference in the C++ sense either. Because list.append() is a mutating method — it changes the object in place, rather than creating a new one — and both names point at that one object,the change is visible through either name. No return statement is needed, because nothing new was ever created; the one existing object was simply edited.")

'''3.3 The Slice Experiment'''
print(" 3.3 -- SLICE EXPERIMENT -- ")

dna_database = ['AATCCG', 'TGGCTA']
print(f"Global Scope (Before) - ID: {id(dna_database)} | Data: {dna_database}")

analyze_sequence(dna_database[:], 'CGAT')

print(f"Global Scope (After) - ID: {id(dna_database)} | Data: {dna_database}")

''' 3.4 Bonus Experiment: Mutation vs. Reassignment'''
def analyze_sequence_rebind(sequence_list, marker):
    print(f"\nInside Rebind (Start) - ID: {id(sequence_list)} | Data: {sequence_list}")
    sequence_list = sequence_list + [marker] #REBINS the local name
    print(f"Inside Rebind (End) - ID: {id(sequence_list)} | Data: {sequence_list}")

print("\n -- BONUS: MUTATION VS REASSIGNMENT -- ")
dna_database = ['AATCCG', 'TGGCTA']
print(f"Global Scope (Before) - ID: {id(dna_database)} | Data: {dna_database}")
analyze_sequence_rebind(dna_database, 'CGAT')
print(f"Global Scope (After) - ID: {id(dna_database)} | Data: {dna_database}")


''' -- Edge Cases to Consider -- '''
print("\n -- EDGE CASE 1 -- ")

empty_result = search4letters('')

print("search4letters(''):", empty_result)

print("\n -- EDGE CASE 2 -- ")

mixed_result = search4letters('TGGACC', letters='GC')

print("search4letters('TGGACC', letters='GC'):", mixed_result)


print("\n -- EDGE CASE 3 -- ")

dna_database = ['AATCCG', 'TGGCTA']

print("Original database:", dna_database)

analyze_sequence(dna_database[:], 'CGAT')
analyze_sequence(dna_database[:], 'AAAA')

print("\nDatabase after repeated slice calls:", dna_database)
