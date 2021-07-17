from otree.api import *
import numpy as np

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Econ400'
    players_per_group = 6
    num_rounds = 1
    instructions_template = 'Econ400/instructions.html'
    instforgame_template = 'Econ400/instforgame.html'
    exercise_template = 'Econ400/exercise.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(label="Please enter your name.", blank=True)
    surname = models.StringField(label="Please enter your surname.", blank=True)
    age = models.IntegerField(label="What is your age?", blank=True)
    gender = models.StringField(choices=[["female", "female"], ["male", "male"], ["other", "other"]])
    school = models.StringField(label="Please write your university's name. ", blank=True)
    department = models.StringField(label="What is your department?", blank=True)
    Grade = models.StringField(label="Please select your grade.",
                               choices=[["0", "Prep school"], ["1", "1"], ["2", "2"], ["3", "3"], ["4", "4"],
                                        ["Masters Degree", "Masters Degree"], ["Doctors Degree", "Doctors Degree"]])
    riskchoice = models.StringField(label="In your daily life, do you avoid risk? ",
                                    widget=widgets.RadioSelectHorizontal,
                                    choices=[["1", "Never, I always take risk"], ["2", "Rarely"], ["3", "Sometimes"],
                                             ["4", "Usually"], ["5", "Always, I never take risk"]])
    gg = models.StringField(label="Do you think that women avoid risk more than men?", widget=widgets.RadioSelect,
                            choices=[["1", "Yes"], ["2", "No"]])
    gh = models.StringField(label="Have you participated a similar game before?", widget=widgets.RadioSelect,
                            choices=[["1", "Yes"], ["2", "No"]])

    k1 = models.IntegerField(label="Everyone in the group, including you, chooses A. What is your earning?", blank=True)
    k2 = models.IntegerField(label="You choose A, all others choose B. What is your earning?", blank=True)
    k3 = models.IntegerField(label="You choose B. all others choose A. What is your earning?", blank=True)
    k4 = models.IntegerField(label="Everyone in the group, including you, choose B. What is your earning?",
                             blank=True)
    k5 = models.IntegerField(label="You choose B. 1 person in your group choose B too. What is your earning?",
                             blank=True)
    k6 = models.IntegerField(label="You choose B. 2 other people in your group choose B . What is your earning?",
                             blank=True)
    k7 = models.IntegerField(label="You choose B. 3 people in your group choose B too. What is your earning?",
                             blank=True)

    choice = models.StringField(label="please choose one", widget=widgets.RadioSelectHorizontal,
                                choices=[["A", "A"], ["B", "B"]])

    r1 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=[["A", "A"], ["B", "B"]])
    r2 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=[["A", "A"], ["B", "B"]])
    r3 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=[["A", "A"], ["B", "B"]])
    r4 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=[["A", "A"], ["B", "B"]])
    r5 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=[["A", "A"], ["B", "B"]])
    r6 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=[["A", "A"], ["B", "B"]])
    r7 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=[["A", "A"], ["B", "B"]])
    r8 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=[["A", "A"], ["B", "B"]])
    r9 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=[["A", "A"], ["B", "B"]])
    r10 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=[["A", "A"], ["B", "B"]])

    guess1 = models.StringField(label="What is your estimation about Mustafa's choice?",
                                widget=widgets.RadioSelectHorizontal, choices=[["A", "Option A"], ["B", "Option B"]])
    guess2 = models.StringField(label="What is your estimation about Zeynep's choice?",
                                widget=widgets.RadioSelectHorizontal, choices=[["A", "Option A"], ["B", "Option B"]])
    guess3 = models.StringField(label="What is your estimation about Ahmet's choice?",
                                widget=widgets.RadioSelectHorizontal, choices=[["A", "Option A"], ["B", "Option B"]])
    guess4 = models.StringField(label="What is your estimation about Emine's choice?",
                                widget=widgets.RadioSelectHorizontal, choices=[["A", "Option A"], ["B", "Option B"]])
    guess5 = models.StringField(label="What is your estimation about Elif's choice?",
                                widget=widgets.RadioSelectHorizontal, choices=[["A", "Option A"], ["B", "Option B"]])
    guess6 = models.StringField(label="What is your estimation about Ayşe's choice?",
                                widget=widgets.RadioSelectHorizontal, choices=[["A", "Option A"], ["B", "Option B"]])
    result = models.IntegerField(initial=0)
    payoffPlayer = models.IntegerField(initial=0)
    random_dice_player = models.IntegerField(initial=0)
    random_row_player = models.IntegerField(initial=0)

    def b_counter(self):
        result = 0
        for p in self.get_others_in_group():
            if p.choice == "B":
                result += 1
        return result

    def calculate_exercise(self):
        result = 0
        random_dice = np.random.randint(low=1, high=11)
        random_selection = np.random.randint(low=1, high=11)
        self.random_dice_player = random_dice
        self.random_row_player = random_selection
        r_list = []
        r_list.append(self.r1)
        r_list.append(self.r2)
        r_list.append(self.r3)
        r_list.append(self.r4)
        r_list.append(self.r5)
        r_list.append(self.r6)
        r_list.append(self.r7)
        r_list.append(self.r8)
        r_list.append(self.r9)
        r_list.append(self.r10)


        for i in range(10):
            if random_selection == i + 1:
                if random_dice > i + 1:
                    if r_list[i] == "A":
                        result += 32
                    elif r_list[i] == "B":
                        result += 2
                else:
                    if r_list[i] == "A":
                        result += 40
                    elif r_list[i] == "B":
                        result += 77
        return result

    def calculate_result(self):
        result = 0
        for p in self.get_others_in_group():
            if p.id_in_group == 1:
                if p.choice == self.guess1:
                    result += 2
            elif p.id_in_group == 2:
                if p.choice == self.guess2:
                    result += 2
            elif p.id_in_group == 3:
                if p.choice == self.guess3:
                    result += 2
            elif p.id_in_group == 4:
                if p.choice == self.guess4:
                    result += 2
            elif p.id_in_group == 5:
                if p.choice == self.guess5:
                    result += 2
            elif p.id_in_group == 6:
                if p.choice == self.guess6:
                    result += 2

        if self.choice == "A":
            result += 8
        elif self.choice == "B":
            if self.b_counter() >= 3:
                result += 24
            else:
                result += 2
        return result

    def calculate_payoff(self):
        return self.calculate_result() / 2 + self.calculate_exercise() / 8 + 5


# FUNCTIONS

def other_player(player: Player):
    return player.get_others_in_group()[0]


def get_player(self):
    return self.get_players()[0]


# PAGES
class Introduction(Page):
    timeout_seconds = 90


class MyPage(Page):
    form_model = 'player'
    form_fields = ['k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7']

    @staticmethod
    def error_message(player, values):
        solutions = dict(k1=8, k2=8, k3=2, k4=24, k5=2, k6=2, k7=24)

        return {f: 'Wrong answer' for f in solutions if values[f] != solutions[f]}


class MiniGuessGame(Page):
    form_model = 'player'
    form_fields = ['guess2', 'guess3', 'guess4', 'guess5', 'guess6']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1


class MiniGuessGame2(Page):
    form_model = 'player'
    form_fields = ['guess1', 'guess3', 'guess4', 'guess5', 'guess6']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2


class MiniGuessGame3(Page):
    form_model = 'player'
    form_fields = ['guess1', 'guess2', 'guess4', 'guess5', 'guess6']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 3


class MiniGuessGame4(Page):
    form_model = 'player'
    form_fields = ['guess1', 'guess2', 'guess3', 'guess5', 'guess6']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 4


class MiniGuessGame5(Page):
    form_model = 'player'
    form_fields = ['guess1', 'guess2', 'guess3', 'guess4', 'guess6']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 5


class MiniGuessGame6(Page):
    form_model = 'player'
    form_fields = ['guess1', 'guess2', 'guess3', 'guess4', 'guess5']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 6


class Game(Page):
    form_model = 'player'
    form_fields = ['choice']


class Exercise(Page):
    form_model = 'player'
    form_fields = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10']


class Questions(Page):
    form_model = 'player'
    form_fields = ['name', 'surname', 'age', 'gender', 'school', 'department', 'Grade', 'riskchoice', 'gg', 'gh']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):

    @staticmethod
    def vars_for_template(player: Player):
        return dict(others=player.get_others_in_group(),
                    result=player.calculate_result(), exercise_result=player.calculate_exercise(),
                    payoff=player.calculate_payoff())

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1


class Result2(Page):

   @staticmethod
    def vars_for_template(player: Player):
        return dict(others=player.get_others_in_group(),
                    result=player.calculate_result(), exercise_result=player.calculate_exercise(),
                    payoff=player.calculate_payoff())

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2


class Result3(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(others=player.get_others_in_group(),
                    result=player.calculate_result(), exercise_result=player.calculate_exercise(),
                    payoff=player.calculate_payoff())

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 3

class Result4(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(others=player.get_others_in_group(),
                    result=player.calculate_result(), exercise_result=player.calculate_exercise(),
                    payoff=player.calculate_payoff())

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 4


class Result5(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(others=player.get_others_in_group(),
                    result=player.calculate_result(), exercise_result=player.calculate_exercise(),
                    payoff=player.calculate_payoff())

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 5

class Result6(Page):

    @staticmethod
    def vars_for_template(player: Player):
        return dict(others=player.get_others_in_group(),
                    result=player.calculate_result(), exercise_result=player.calculate_exercise(),
                    payoff=player.calculate_payoff())

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 6


page_sequence = [Introduction, MyPage, Game, MiniGuessGame, MiniGuessGame2, MiniGuessGame3,
                 MiniGuessGame4, MiniGuessGame5, MiniGuessGame6, 
                 Exercise, Questions, ResultsWaitPage, Results, Result2, Result3, Result4,
                 Result5, Result6]
