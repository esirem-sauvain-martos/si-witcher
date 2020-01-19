class Army:

    def __init__(self, chief, moral_base):
        self._chief = chief
        self._moral_base = moral_base

    def get_total_moral(self):
        return self._moral_base * self._chief.moral_boost

    # Chief
    def get_chief(self):
        return self._chief

    def set_chief(self, chief):
        self._chief = chief

    chief = property(get_chief, set_chief)

    # Moral Base
    def get_moral_base(self):
        return self._moral_base

    def set_moral_base(self, moral_base):
        self._moral_base = moral_base

    moral_base = property(get_moral_base, set_moral_base)

    def __str__(self):
        return "Army : chief = {}, moral_base = {}".format(
            self._chief,
            self._moral_base
        )