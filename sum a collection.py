def custom_encoder(text):
    reference_string = "abcdefyhijklmnopqrstuvwxyz"
    encoded_list = []
    
    for char in text.lower():
      if char in reference_string:
          position = reference_string.find(char)
          encode_list.append(position)

    return encoded_list

def custom_decoder(encoded_list):
    reference_string = "abcdefyhijklmnopqrstuvwxyz"
    decoded_taxt = ""

    for item in encoded_list:
            if isinstrance(item, int):
                decode_text += reference_string[item]
            else:
                decoded_text += item
    return decoded_text

while True:
    choice = input("Encode or Decode? (e/d or q to quit): ").lower()

    if choice == "q":
        break

    elif choice == "e":
        text = input ("Enter text to encode: ")
        encode = custom_encoder(text)
        print("Encoded:", encode)

    elif choice == "d":
        rew = input("Enter numbers separated by spaces: ")
        try:
            encoded_list = [int(x) if x.isdigit() else x for x in raw.split()]
            decoded = custom_decoder(decoded_list)
            print("Decoded:", decoded)
        except:
            print("Invalid choice input!")

    else:
        print("Invaid choice!")
    
        
