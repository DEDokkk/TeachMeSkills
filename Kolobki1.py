import enum


class Constants(enum.Enum):
    solved_status = 'solved'
    in_progress_status = 'in progress'
    not_started_status = 'not started'
    starley_rank = 'starley'
    capitan_rank = 'capitan'
    general_rank = 'general'


class Kolobok:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank


class Investigation:
    def __init__(self, complexity):
        if complexity not in range(0, 300):
            raise ValueError('Сложность дела должна быть в диапазоне от 0 до 300')
        self.complexity = complexity
        self.status = Constants.not_started_status.value
        self.detectives = []

    def add_detective(self, rank):
        self.rank = rank
        if self.complexity > 0 and self.status != Constants.solved_status.value:
            if self.rank == Constants.starley_rank.value:
                self.complexity -= 1
            if self.rank == Constants.capitan_rank.value:
                self.complexity -= 2
            if self.rank == Constants.general_rank.value:
                self.complexity -= 3
            if self.complexity <= 0:
                self.status = Constants.solved_status.value
            else:
                self.status = Constants.in_progress_status.value
        else:
            raise Exception
        return self.status


