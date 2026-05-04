def remove_duplicates_in_list(item : list[object]) -> list[object]:
    unique = set(item)
    return list(unique)

if __name__ == "__main__":
    item = ["vilas", "vilas", 1, 32, 1, 55.0, "v"]
    print(remove_duplicates_in_list(item))