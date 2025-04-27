# Create a class 'Programmer' for storing information of few programmers working at Microsoft.

class ProgrammerInMicrosoft:
    def __init__(self, name, age, occupation, package, employId, githubId, email):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.package = package
        self.employId = employId
        self.githubId = githubId
        self.email = email


employee1 = ProgrammerInMicrosoft(
    name="Alice Johnson",
    age=29,
    occupation="Software Engineer",
    package=160000,
    employId="MS1234",
    githubId="alicejohnson",
    email="alice.johnson@microsoft.com"
)

employee2 = ProgrammerInMicrosoft(
    name="Bob Smith",
    age=35,
    occupation="Senior Developer",
    package=200000,
    employId="MS5678",
    githubId="bobsmithdev",
    email="bob.smith@microsoft.com"
)

employee3 = ProgrammerInMicrosoft(
    name="Charlie Lee",
    age=26,
    occupation="Cloud Engineer",
    package=150000,
    employId="MS9101",
    githubId="charlielee-cloud",
    email="charlie.lee@microsoft.com"
)