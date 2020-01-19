class Character:

    def __init__(self, name, firstname, age, job, moral_boost):
        self._name = name
        self._firstname = firstname
        self._age = int(age)
        self._job = job
        self._moral_boost = float(moral_boost)

    # Name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    name = property(get_name, set_name)

    # Firstname
    def get_firstname(self):
        return self._firstname

    def set_firstname(self, firstname):
        self._firstname = firstname

    firstname = property(get_firstname, set_firstname)

    # Age
    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age
    
    age = property(get_age, set_age)

    # Job
    def get_job(self):
        return self._job

    def set_job(self, job):
        self._job = job

    job = property(get_job, set_job)

    # Moral Boost
    def get_moral_boost(self):
        return self._moral_boost

    def set_moral_boost(self, moral_boost):
        self._moral_boost = moral_boost

    moral_boost = property(get_moral_boost, set_moral_boost)

    def __str__(self):
        return "Character : name = {}, firstname = {}, age = {}, job = {}, moral_boost = {}".format(
            self._name,
            self._firstname,
            self._age,
            self._job,
            self._moral_boost
        )
