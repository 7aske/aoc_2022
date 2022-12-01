def main():

	with open("input.txt") as file:
		inp = file.read()

		elves = [[]]

		for i, line in enumerate(inp.split("\n")):
			if line == "":
				elves.append([])
				continue

			elves[len(elves) - 1].append(int(line))

		print(sum(sorted(map(sum, elves), reverse=True)[0:3]))


if __name__ == '__main__':
	main()
