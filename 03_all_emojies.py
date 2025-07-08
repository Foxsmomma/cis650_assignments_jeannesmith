#Consider this list of emojis and their hexadecimal representations

# Write a script that will ask the user for a keyword
# the script will use the find method to search each name and then prints 
# the name and emoji on screen. print(chr(0x1F600), end=' ')

# After completing this script, git commit with 'after_03_all_emojis' as the message 
# and git push the repo #
face_emojis= [
    {"name": "Grinning Face", "hex": "U+1F600"},
    {"name": "Beaming Face with Smiling Eyes", "hex": "U+1F601"},
    {"name": "Face with Tears of Joy", "hex": "U+1F602"},
    {"name": "Rolling on the Floor Laughing", "hex": "U+1F923"},
    {"name": "Smiling Face with Open Mouth", "hex": "U+1F603"},
    {"name": "Smiling Face with Open Mouth & Smiling Eyes", "hex": "U+1F604"},
    {"name": "Smiling Face with Open Mouth & Cold Sweat", "hex": "U+1F605"},
    {"name": "Smiling Face with Open Mouth & Tightly-Closed Eyes", "hex": "U+1F606"},
    {"name": "Winking Face", "hex": "U+1F609"},
    {"name": "Smiling Face with Smiling Eyes", "hex": "U+1F60A"},
    {"name": "Face Savoring Food", "hex": "U+1F60B"},
    {"name": "Relieved Face", "hex": "U+1F60C"},
    {"name": "Smiling Face with Heart-Eyes", "hex": "U+1F60D"},
    {"name": "Face Blowing a Kiss", "hex": "U+1F618"},
    {"name": "Kissing Face", "hex": "U+1F617"},
    {"name": "Kissing Face with Smiling Eyes", "hex": "U+1F619"},
    {"name": "Kissing Face with Closed Eyes", "hex": "U+1F61A"},
    {"name": "Face with Stuck-Out Tongue", "hex": "U+1F61B"},
    {"name": "Face with Stuck-Out Tongue & Winking Eye", "hex": "U+1F61C"},
    {"name": "Face with Stuck-Out Tongue & Tightly-Closed Eyes", "hex": "U+1F61D"},
    {"name": "Money-Mouth Face", "hex": "U+1F911"},
    {"name": "Hugging Face", "hex": "U+1F917"},
    {"name": "Thinking Face", "hex": "U+1F914"},
    {"name": "Shushing Face", "hex": "U+1F92B"},
    {"name": "Zany Face", "hex": "U+1F92A"},
    {"name": "Smirking Face", "hex": "U+1F60F"},
    {"name": "Unamused Face", "hex": "U+1F612"},
    {"name": "Face with Raised Eyebrow", "hex": "U+1F928"},
    {"name": "Neutral Face", "hex": "U+1F610"},
    {"name": "Expressionless Face", "hex": "U+1F611"},
    {"name": "Face Without Mouth", "hex": "U+1F636"},
    {"name": "Smiling Face with Sunglasses", "hex": "U+1F60E"},
    {"name": "Nerd Face", "hex": "U+1F913"},
    {"name": "Face with Monocle", "hex": "U+1F9D0"},
    {"name": "Disappointed Face", "hex": "U+1F61E"},
    {"name": "Worried Face", "hex": "U+1F61F"},
    {"name": "Sad but Relieved Face", "hex": "U+1F625"},
    {"name": "Crying Face", "hex": "U+1F622"},
    {"name": "Loudly Crying Face", "hex": "U+1F62D"},
    {"name": "Face Screaming in Fear", "hex": "U+1F631"},
    {"name": "Fearful Face", "hex": "U+1F628"},
    {"name": "Flushed Face", "hex": "U+1F633"},
    {"name": "Sleeping Face", "hex": "U+1F634"},
    {"name": "Dizzy Face", "hex": "U+1F635"},
    {"name": "Pensive Face", "hex": "U+1F614"},
    {"name": "Confused Face", "hex": "U+1F615"},
    {"name": "Face with Rolling Eyes", "hex": "U+1F644"},
    {"name": "Grimacing Face", "hex": "U+1F62C"},
    {"name": "Lying Face", "hex": "U+1F925"},
    {"name": "Overheated Face", "hex": "U+1F975"},
    {"name": "Cold Face", "hex": "U+1F976"},
    {"name": "Exploding  Head", "hex": "U+1F92F"},]

userkeyword = input("Please enter a keyword: ")
selected = next((i for i in face_emojis if i["name"] == userkeyword), None)
print(selected.get("name")+chr(int(selected.get("hex")[2:], 16)), end =' ')