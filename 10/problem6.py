# Can you change the self-parameter inside a class to something else (say 'harry'). Try changing self to 'slf' or 'harry' and see the effects.

# Yup we could, self is just a parameter name, we could also say it ballu or sallu



class sample:
    name = "User"

    def greet(slf):
        print(f"Hello {slf.name}!")

a = sample()
a.name="Saksham"
a.greet()