genome = input().upper()
sum = genome.count('G') + genome.count('C')
part = sum / len(genome) * 100
print(part)