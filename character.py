
class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what character will say
    def set_conversation(self, conversation):
        self.conversation = conversation;

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + "]:" + self.conversation)
        else:
            print(self.name + "doesn't wants to talk") 