def character_stuffing(original_data, start_char, end_char, escape_char):
    stuffed_data = []
    stuffed_data.append(start_char)
    for char in original_data:
        if char == start_char or char == end_char or char == escape_char:
            stuffed_data.append(escape_char)
            stuffed_data.append(char)
            stuffed_data.append(end_char)
    return ''.join(stuffed_data)
def character_destuffing(stuffed_data, start_char, end_char, escape_char):
    original_data = []
    i = 1 # Skip the start character
    while i < len(stuffed_data) - 1: # Skip the end character
        if stuffed_data[i] == escape_char:
            i += 1
            original_data.append(stuffed_data[i])
            i += 1
    return ''.join(original_data)
if __name__ == "__main__":
    original_data = "Hello<World!"
    start_char = '<'
    end_char = '>'
    escape_char = '\\'
    print("Original Data:", original_data)
    stuffed_data = character_stuffing(original_data, start_char, end_char, escape_char)
    print("Stuffed Data:", stuffed_data)
    destuffed_data = character_destuffing(stuffed_data, start_char, end_char, escape_char)
    print("Destuffed Data:", destuffed_data)
