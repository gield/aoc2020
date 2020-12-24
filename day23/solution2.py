with open("input.txt", "r") as f:
    cups = [int(c) for c in f.read().strip()]

for i in range(len(cups), 1_000_000):
    cups.append(i + 1)


class Cup:
    def __init__(self, value: int):
        self.value = value
        self.previous = None
        self.next = None


class CircleOfCups:
    def __init__(self, list_of_cups):
        self.cup_dict = {}
        self.start_cup = self.create_circle(list_of_cups)

    def create_circle(self, list_of_cups):
        start_cup = Cup(list_of_cups[0])
        self.cup_dict[list_of_cups[0]] = start_cup
        previous_cup = start_cup
        for cup_value in list_of_cups[1:]:
            new_cup = Cup(cup_value)
            self.cup_dict[cup_value] = new_cup
            CircleOfCups.link_cups(previous_cup, new_cup)
            previous_cup = new_cup
        CircleOfCups.link_cups(previous_cup, start_cup)
        return start_cup

    @staticmethod
    def link_cups(cup1, cup2):
        cup1.next = cup2
        cup2.previous = cup1


circle = CircleOfCups(cups)
num_cups = len(circle.cup_dict)

current_cup = circle.start_cup
for move in range(10_000_000):
    first_picked_up, last_picked_up = current_cup.next, current_cup.next.next.next
    pick_up_values = {first_picked_up.value, first_picked_up.next.value, last_picked_up.value}
    CircleOfCups.link_cups(current_cup, last_picked_up.next)

    for i in range(num_cups - 4):
        # Lower destination value by 1 each time
        # Note: `or num_cups` makes sure we go from 1 to 9 instead of 1 to 0
        destination_value = (current_cup.value - i - 1) % num_cups or num_cups
        if destination_value not in pick_up_values:
            break

    destination_cup = circle.cup_dict[destination_value]
    CircleOfCups.link_cups(last_picked_up, destination_cup.next)
    CircleOfCups.link_cups(destination_cup, first_picked_up)

    current_cup = current_cup.next

cup1 = circle.cup_dict[1]
print(cup1.next.value * cup1.next.next.value)
