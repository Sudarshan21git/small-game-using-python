alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text,shift,encode_or_decode):
    chipper = "" 
    if encode_or_decode=="decode":
            shift*=-1
    for letter in original_text:
        if letter in alphabet:
                    shift_position = (alphabet.index(letter) + shift) % 26 
                    chipper += alphabet[shift_position]
        
        else:
            chipper+=letter
                
        
      
    print(f"the {encode_or_decode}d text is:"+str(chipper))
should_coutinue=True
while should_coutinue:
    direction = input("Type 'encode' or 'decode':\n").lower()
    original_text = input("ENTER THE MESSAGE: ").lower()
    shift = int(input("Type your shift number:\n"))
    
    caesar(original_text=original_text, shift=shift,encode_or_decode=direction)
    restart=input("Type 'yes' if you want to go again.otherwise type'no.\n").lower()
    if restart=="no":
        should_coutinue=False
        print("GoodBye")